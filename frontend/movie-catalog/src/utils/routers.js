import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/authStore.js";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "Home",
      component: () => import("@/views/Home.vue")
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("@/views/Login.vue")
    },
    {
      path: "/register",
      name: "Register",
      component: () => import("@/views/Register.vue")
    },
    {
      path: "/movies/:id",
      name: "MovieDetail",
      component: () => import("@/views/MovieDetail.vue")
    },
    {
      path: "/movies/create",
      name: "MovieCreate",
      component: () => import("@/views/MovieForm.vue"),
      meta: { requiresAuth: true }
    },
    {
      path: "/movies/:id/edit",
      name: "MovieEdit",
      component: () => import("@/views/MovieForm.vue"),
      meta: { requiresAuth: true }
    }
  ],
});

// Navigation guard для перевірки авторизації
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth && !authStore.user) {
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;