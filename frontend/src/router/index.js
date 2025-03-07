import { createRouter, createWebHistory } from 'vue-router';
import { routesConfig } from '../lib/routesConfig';

// create a new router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), // use HTML5 history mode
  routes: [
    {
      path: '/',
      redirect: '/dashboard', // redirect to the dashboard route when the app starts
      component: () => import('../layouts/BaseLayout.vue'),
      children: routesConfig
    },
    {
      path: '/error',
      component: () => import('../views/ErrorPage.vue')
    }
  ]
});

export default router;
