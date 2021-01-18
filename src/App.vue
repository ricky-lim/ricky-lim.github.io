<template>
  <v-app>
    <v-navigation-drawer app v-model="drawer" absolute temporary>
      <v-list-item
          v-for="item in navItems"
          :key="item.title"
          :to="item.route"
          class="ma-4"
      >
        <v-list-item-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>
            {{ item.title }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item class="ma-4">
        <v-switch
            v-model="$vuetify.theme.dark"
            :label="`${$vuetify.theme.dark ? 'Dark' : 'Light'} Mode`"
            hide-details
        ></v-switch>
      </v-list-item>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-avatar v-if="$vuetify.theme.dark">
        <img :src="require('@/assets/logo.png')" alt="logo">
      </v-avatar>
      <v-avatar v-else>
        <img :src="require('@/assets/logo-transparent.png')" alt="logo">
      </v-avatar>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <transition name="fade" mode="out-in">
          <router-view></router-view>
        </transition>
      </v-container>
    </v-main>

    <v-footer app>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: false,
    mode: false,
    navItems: [
      {icon: 'mdi-home', title: 'Home', route: '/'},
      {icon: 'mdi-account-box', title: 'About', route: '/about'}
    ]

  }),
  created() {
    this.$vuetify.theme.dark = false;
  }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

</style>
