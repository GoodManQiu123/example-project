// Define the routes for the application
export const routesConfig = [
  {
    path: '/dashboard',
    name: 'dashboard',
    icon: 'dashboard',
    component: () => import('@/views/PaperDashboard.vue'),
    meta: {
      keepAlive: true,
      title: 'Dashboard',
    }
  },
  {
    path: '/topic',
    name: 'topic',
    icon: 'topic',
    redirect: '/topic/same-topic', // redirect to the first child route
    meta: {
      title: 'Topic',
    },
    children: [
      {
        path: '/topic/same-topic',
        name: 'same-topic',
        icon: 'chat',
        meta: {
          title: 'Same Topic',
        },
        component: () => import('@/views/topic/SameTopic.vue')
      },
      {
        path: '/topic/connections',
        name: 'connections',
        icon: 'forum',
        meta: {
          title: 'Topic Connections',
        },
        component: () => import('@/views/topic/TopicConnections.vue')
      },
    ]
  },
  {
    path: '/author',
    name: 'author',
    icon: 'person',
    redirect: '/author/co-authors', // redirect to the first child route
    meta: {
      title: 'Author',
    },
    children: [
      {
        path: '/author/co-authors',
        name: 'co-authors',
        icon: 'groups',
        meta: {
          title: 'Co-Authors',
        },
        component: () => import('@/views/author/CoAuthors.vue')
      },
      {
        path: '/author/affiliations',
        name: 'affiliations',
        icon: 'apartment',
        meta: {
          title: 'Affiliations',
        },
        component: () => import('@/views/author/AuthorAffiliation.vue')
      }
    ]
  },
  {
    path: '/reference',
    name: 'reference',
    icon: 'link',
    redirect: '/reference/cited', // redirect to the first child route
    meta: {
      title: 'Reference',
    },
    children: [
      {
        path: '/reference/cited',
        name: 'cited',
        icon: 'vertical_align_top',
        meta: {
          title: 'Cited Tree',
        },
        component: () => import('@/views/reference/CitedTree.vue')
      },
      {
        path: '/reference/cited-by',
        name: 'cited-by',
        icon: 'vertical_align_bottom',
        meta: {
          title: 'Cited-By Tree',
        },
        component: () => import('@/views/reference/CitedByTree.vue')
      },
    ]
  },



];
