<script setup>
import { onMounted, ref, watch } from "vue";
import { routesConfig } from "@/lib/routesConfig.js";
import { useRouter } from "vue-router";

const router = useRouter(); // Vue Router instance for navigation
const header = ref('Null'); // header title
const activeElement = ref(null); // active element in the sidebar
const activeRouteName = ref(''); // active route name
const accordionValue = ref([]); // accordion value in a list e.g. [true, false, false]
const minimized = ref(false); // sidebar minimized state

// method to generate the active route
function generateActive() {
  // if the route has children
  if (router.currentRoute.value.matched.length > 2) {
    const parent = router.currentRoute.value.matched[1].name;
    const child = router.currentRoute.value.matched[2].name;
    // find the index of the parent route
    const parentIndex = routesConfig.findIndex((route) => route.name === parent);
    accordionValue.value[parentIndex] = true; // open the parent route in the sidebar
    activeRouteName.value = child; // set the active route name
  } else {
    // if the route has no children, set the active route name
    activeRouteName.value = router.currentRoute.value.matched[1].name;
  }
}

// method to check if the route is active
function isRouteActive(route) {
  return route.name === activeRouteName.value;
}

// method to set the active route
function setRouteActive(route) {
  if (route.children) return; // if the route has children, return
  activeRouteName.value = route.name;
  window.scrollTo(0, 0);
  router.push(route.path);
}

// method to toggle the sidebar
function toggleSidebar() {
  minimized.value = !minimized.value;
  localStorage.setItem('minimized', minimized.value.toString()); // save the minimized state to the local storage
}

// watch the route change and update the header title
watch(() => router.currentRoute.value, (newRoute) => {
  const matchedRoute = newRoute.matched.slice().reverse().find(r => r.meta && r.meta.title);
  if (matchedRoute && matchedRoute.meta && matchedRoute.meta.title) {
    header.value = matchedRoute.meta.title;
  }
  generateActive(); // generate the active route with the new route
}, { immediate: true });

// when the component is mounted
onMounted(() => {
  // get the saved accordion value from the local storage
  const savedAccordionValue = localStorage.getItem('accordionValue');
  if (savedAccordionValue) {
    accordionValue.value = JSON.parse(savedAccordionValue);
  } else {
    accordionValue.value = new Array(routesConfig.length).fill(true);
  }
  // get the saved minimized state from the local storage
  const savedMinimized = localStorage.getItem('minimized');
  if (savedMinimized) {
    minimized.value = savedMinimized === 'true';
  }
  // set the accordion value to the local storage when it changes
  watch(accordionValue, (newValue) => {
    localStorage.setItem('accordionValue', JSON.stringify(newValue));
  }, { deep: true, immediate: true });
});

</script>

<template>
  <!-- layout component -->
  <VaLayout
      :left="{ fixed: true, order: 2 }"
      :top="{ fixed: true, order: 1 }"
  >
    <!-- top app bar of the layout -->
    <template #top>
      <VaNavbar
          class="h-[58px] py-2"
          shadowed
      >
        <template #left>
          <!-- button to toggle the sidebar -->
          <VaNavbarItem>
            <VaButton
                :icon="minimized ? 'menu' : 'menu_open'"
                @click="toggleSidebar"
            />
          </VaNavbarItem>
          <VaNavbarItem>
            <p class="font-black text-xl">SCHOLARLY NET</p>
          </VaNavbarItem>
        </template>
        <template #right>
          <!-- user avatar -->
          <VaNavbarItem>
            <VaAvatar
                size="small"
                class="mr-2 rounded"
                square
            >
              A
            </VaAvatar>
          </VaNavbarItem>
        </template>
      </VaNavbar>
    </template>
    <!-- sidebar of the layout -->
    <template #left>
      <VaSidebar
          :minimized="minimized"
          minimized-width="80px"
      >
        <VaAccordion
            v-model="accordionValue"
            multiple
        >
          <VaCollapse
              v-for="(route, idx) in routesConfig"
              :key="idx"
              body-color="#fff"
          >
            <template #header>
              <!-- sidebar section item for the route -->
              <VaSidebarItem
                  :active="isRouteActive(route)"
                  @click="setRouteActive(route)"
              >
                <VaSidebarItemContent>
                  <VaIcon :name="route.icon" />
                  <VaSidebarItemTitle>
                    {{ route.meta.title }}
                  </VaSidebarItemTitle>
                  <VaIcon
                      v-if="route.children"
                      :name="accordionValue[idx] ? 'expand_less' : 'expand_more'"
                  />
                </VaSidebarItemContent>
              </VaSidebarItem>
            </template>
            <!-- sidebar section item for the route children -->
            <template #body>
              <VaSidebarItem
                  v-for="(child, index) in route.children"
                  :key="index"
                  :active="isRouteActive(child)"
                  @click="setRouteActive(child)"
              >
                <VaSidebarItemContent class="ml-3 overflow-hidden">
                  <VaIcon :name="child.icon" />
                  <VaSidebarItemTitle>
                    {{ child.meta.title }}
                  </VaSidebarItemTitle>
                </VaSidebarItemContent>
              </VaSidebarItem>
            </template>
          </VaCollapse>
        </VaAccordion>
        <VaSpacer />
        <!-- sidebar bottom section item for the settings -->
        <VaSidebarItem
            :active="'Settings' === activeElement"
            @click="console.log('Settings coming soon...')"
        >
          <VaSidebarItemContent>
            <VaIcon name="settings" />
            <VaSidebarItemTitle>Settings</VaSidebarItemTitle>
          </VaSidebarItemContent>
        </VaSidebarItem>
      </VaSidebar>
    </template>
    <!-- main content area of the layout -->
    <template #content>
      <main class="p-4">
        <h1 class="text-3xl font-black ml-2 mb-3 uppercase">{{header}}</h1>
        <div class="h-[80vh] bg-white shadow-lg overflow-auto">
          <!-- router view to display the route component with keep-alive -->
          <router-view v-slot="{ Component }">
            <!-- keep-alive if the route has keep-alive meta -->
            <keep-alive>
              <component :is="Component"  v-if="$route.meta.keepAlive"/>
            </keep-alive>
            <!-- normal component if the route has no keep-alive meta -->
            <component :is="Component"  v-if="!$route.meta.keepAlive"/>
          </router-view>
        </div>
      </main>
    </template>
  </VaLayout>
</template>
