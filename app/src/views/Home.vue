<template>
  <div class="meter">
    <figure class="highcharts-figure">
      <div id="container"></div>
    </figure>
  </div>
</template>

<script>
import axios from 'axios'
import Highcharts from 'highcharts'

export default {
  name: 'Home',
  data () {
    return {
      onTraining: 0,
      curIter: 0,
      curValue: 0.0,
      resURL: 'http://127.0.0.1:8000/api/meter/'
    }
  },
  methods: {
  },
  mounted () {
    var chart = Highcharts.chart('container', {
      chart: {
        type: 'spline',
        animation: Highcharts.svg,
        marginRight: 10,
        events: {
          load: () => {
            setInterval(() => {
              axios.get(this.resURL)
                .then((response) => {
                  if (response.data.iter !== this.curIter) {
                    var series = chart.series[0]
                    this.curIter = response.data.iter
                    this.curValue = response.data.value
                    series.addPoint([this.curIter, this.curValue])
                  }
                })
            }, 3000)
          }
        }
      },
      title: {
        text: 'Simple online plot'
      },
      xAxis: {
      },
      yAxis: {
      },
      series: [{
        name: 'metric',
        data: [{
          iter: 0,
          value: 0.0
        }]
      }]
    })
  },
  components: {
  }
}
</script>
