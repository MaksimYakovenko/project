import {defineStore} from 'pinia';
import apiPrivate, {setAccessTokenToHeaders} from '@/utils/apiPrivate.js';
import apiPublic from "@/utils/apiPublic.js";

export const useAuthStore = defineStore('auth', {
    state: () => ({
        access: null,
        isRefreshing: false,
        queue: [],
        user: null,
        groups: [],
        permissions: [],
    }),

    actions: {
        async register(username, email, password) {
            await apiPublic.post('/register/', {
                username,
                email,
                password,
                password2: password
            });
            return await this.login(username, password);
        },

        async login(username, password) {
            const {data} = await apiPublic.post('/token/', {username, password});

            this.access = data.access;
            setAccessTokenToHeaders(data.access);

            await this.loadUser();

            return true;
        },

        async logout() {
            await apiPrivate.post('/logout/');
            this.access = null;
            setAccessTokenToHeaders(null);
            this.removeUser();
        },

        async refreshAccessToken() {
            if (this.isRefreshing) {
                return new Promise(r => {
                    this.queue.push(r)
                });
            }

            this.isRefreshing = true;
            try {
                const {data} = await apiPublic.post('/token/refresh/');
                this.access = data.access;

                setAccessTokenToHeaders(data.access);

                this.queue.forEach(r => r(data.access));
                this.queue.length = 0;

                return data.access;
            } catch (err) {
                return null;
            } finally {
                this.isRefreshing = false;
            }
        },

        async loadUser() {
            try {
                const response = await apiPrivate.get("/me/");
                this.user = response.data;
                this.groups = response.data.groups;
                this.permissions = response.data.permissions;
            } catch {
                this.removeUser();
            }
        },

        removeUser() {
            this.user = null;
            this.groups = [];
            this.permissions = [];
        },

        hasGroup(name) {
            return this.groups.includes(name);
        },

        hasPermission(perm) {
            return this.permissions.includes(perm);
        }
    }
});