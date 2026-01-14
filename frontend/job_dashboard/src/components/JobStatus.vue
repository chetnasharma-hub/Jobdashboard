<template>
  <div style="width: 400px; margin: auto;">
    <Pie :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import axios from "axios"
import { Pie } from "vue-chartjs"
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement
} from "chart.js"

ChartJS.register(Title, Tooltip, Legend, ArcElement)

export default {
  name: "JobStatusPie",
  components: { Pie },

  data() {
    return {
      chartData: {
        labels: [],
        datasets: [
          {
            data: [],
            backgroundColor: [
              "#6c757d", // Draft
              "#0d6efd", // Requested
              "#198754", // Posted
              "#dc3545"  // Filled
            ]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        plugins: {
          legend: {
            position: "bottom"
          }
        }
      }
    }
  },

  async mounted() {
    const res = await axios.get(
      "http://localhost:8000/job-status-stats/"
    )

    this.chartData.labels = res.data.map(
      item => `${item.status} (${item.percentage}%)`
    )

    this.chartData.datasets[0].data = res.data.map(
      item => item.count
    )
  }
}
</script>
