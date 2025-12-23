import apiPrivate from "@/utils/apiPrivate.js";
import {useAuthStore} from "@/stores/authStore.js";
import axios from "axios";


export function installInterceptors() {

    apiPrivate.interceptors.request.use(async (config) => {
        const authStore = useAuthStore();

        if (!authStore.access) {
            const token = await authStore.refreshAccessToken();
            if (token) {
                config.headers["Authorization"] = `Bearer ${token}`;
            }
            else {
                throw new axios.Cancel();
            }
        }

        return config;
    });

    apiPrivate.interceptors.response.use(res => res, async error => {
        const authStore = useAuthStore();

        if (error.response?.status === 401 && error.config._retry === undefined) {
          error.config._retry = true;
          const newToken = await authStore.refreshAccessToken();
          if (newToken) {
              error.config.headers["Authorization"] = `Bearer ${newToken}`;
              return apiPrivate.request(error.config);
          }
        }

        return Promise.reject(error);
      }
    )
}