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
        backgroundColor: 'black',
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
      plotOptions: {
        series: {
          color: '#00FF00'
        }
      },
      title: {
        text: 'Simple online plot',
        style: {
          color: '#00FF00'
        }
      },
      xAxis: {
        gridLineColor: '#00FF00',
        gridLineWidth: 0.5,
        title: {
          text: 'iteration / epoch',
          style: {
            color: '#00FF00'
          }
        },
        labels: {
          style: {
            color: '#00FF00'
          }
        }
      },
      yAxis: {
        gridLineColor: '#00FF00',
        gridLineWidth: 0.5,
        title: {
          text: 'value',
          style: {
            color: '#00FF00'
          }
        },
        labels: {
          style: {
            color: '#00FF00'
          }
        }
      },
      tooltip: {
        headerFormat: '{point.x} iter<br/>',
        pointFormat: '{point.y:.4f}',
        backgroundColor: 'black',
        borderColor: '#00FF00',
        style: {
          color: '#00FF00'
        }
      },
      series: [{
        name: 'metric',
        marker: {
          radius: 4.0
        },
        data: [{
          iter: 0,
          value: 0.0
        }]
      }],
      credits: {
        enabled: false
      }
    })
  },
  components: {
  }
}
</script>
<style>
body, html {
  background-color: black;
}
</style>
