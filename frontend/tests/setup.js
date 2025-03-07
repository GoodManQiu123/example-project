import { config } from '@vue/test-utils';
import { createRouter, createWebHistory } from 'vue-router';
import { routesConfig } from '@/lib/routesConfig';
import { createVuestic } from 'vuestic-ui'

// configure the router
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes:  [
    {
      path: '/',
      redirect: '/dashboard',
      component: () => import('@/layouts/BaseLayout.vue'),
      children: routesConfig,
    },
    {
      path: '/error',
      component: () => import('@/views/ErrorPage.vue')
    }
  ],
});

// set up the router
export function setupRouter() {
  // router.push('/').then(); // Navigate to initial route
  return router;
}

// use the router with Vue Test Utils
config.global.plugins.push([router]);
config.global.plugins.push(createVuestic({}))
