<template>
  <v-container>
    <p>Progress {{year}}</p>
    <v-progress-linear
        v-model="yearProgress"
        height="25"
        class="white--text"
    >
      <strong>{{ yearProgress.toFixed(2) }}%</strong>
    </v-progress-linear>
  </v-container>
</template>
<script>
export default {
  name: 'YearProgress',
  data: () => ({
    year: new Date().getFullYear(),
    month: new Date().getMonth(),
    date: new Date().getDate()
  }),
  computed: {
    today: function() {
      return new Date(this.year, this.month, this.date)
    },
    firstDateOfYear: function() {
      return new Date(this.year, 0, 1)
    },
    lastDateOfYear: function() {
      return new Date(this.year + 1, 0, 1)
    },
    yearDiff: function () {
      return this.lastDateOfYear - this.firstDateOfYear;
    },
    yearProgress: function() {
      let currentDiff = this.today - this.firstDateOfYear;
      return currentDiff * 100 / this.yearDiff
    }
  }
}
</script>
