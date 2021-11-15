<template>
  <el-container>
    <el-aside width="200px">
      <p>Please input the filter</p>
      <!-- <tr>
        <td width="180">
          <el-input
            v-model="indicatorcode"
            placeholder="indicatorcode"></el-input>
        </td>
      </tr> -->
      <tr>
        <el-select v-model="selectIndicatorcode" placeholder="please select">
          <el-option
            v-for="item in options1"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </tr>
       <!-- <tr>
        <el-select v-model="aveSum" placeholder="please choose ave/sum">
          <el-option
            v-for="item in options2"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </tr> -->
      <tr>
        <td width="180">
          <el-input v-model="startyear" placeholder="startyear"></el-input>
        </td>
      </tr>
      <tr>
        <td width="180">
          <el-input v-model="endyear" placeholder="endyear"></el-input>
        </td>
      </tr>
    </el-aside>
    <el-main>
      <div id="main" style="width: 1500px; height: 600px"></div>
      <div>
        <p>{{ result_data }}</p>
      </div>
    </el-main>
  </el-container>
</template>
<script>
import axios from 'axios'
import * as echarts from 'echarts'
const url = 'http://localhost:5000/data/'
export default {
  data () {
    return {
      result_data: 'Hello world',
      // indicatorcode: '',
      // startyear: '',
      // endyear: '',
      startyear: this.$route.query.startyear,
      endyear: this.$route.query.endyear,
      showdata: true,
      options1: [{
        value: 'UIS.SAP.CE.F',
        label: 'Population of compulsory school age, female (number)'
      }, {
        value: 'UIS.LP.AG15T99',
        label: 'Adult illiterate population, 15+ years, both sexes (number)'
      }, {
        value: 'UIS.NERA.2.F',
        label: 'Adjusted net enrolment rate, lower secondary, female (%)'
      }, {
        value: 'UIS.NIRA.1',
        label: 'Adjusted net intake rate to Grade 1 of primary education, both sexes (%)'
      }, {
        value: 'UIS.FOSGP.56.F400.M',
        label: 'Percentage of male graduates from tertiary education graduating from Science programmes, male (%)'
      }, {
        value: 'UIS.E.1.G1',
        label: 'Enrolment in Grade 1 of primary education, both sexes (number)'
      }, {
        value: 'HH.MICS.YRS.15UP.GIN.Q5',
        label: 'MICS: Gini coefficient of average years of schooling. Age 15+. Quintile 5'
      }],
      selectIndicatorcode: '',
      options2: [{
        value: 'ave',
        label: 'Calculate average value'
      }, {
        value: 'sum',
        label: 'Calculate sum value'
      }],
      aveSum: ''
    }
  },
  mounted () {
    var code1 = this.$route.query.indicatorcode
    var code2 = this.$route.query.startyear
    var code3 = this.$route.query.endyear

    if (typeof (code1) === 'undefined' || code1 === null || code1 === '' || typeof (code2) === 'undefined' || code2 === null || code2 === '' || typeof (code3) === 'undefined' || code3 === null || code3 === '') {
      axios
        .get(url)
        .then((response) => (this.result_data = response.data))
        .catch(function (error) {
          console.log(error)
        })
      this.getEchartData()
    } else {
      var newUrl = url + '?indicatorcode=' + this.$route.query.indicatorcode + '&indicatorcode=' + this.$route.query.startyear + '&indicatorcode=' + this.$route.query.endyear
      axios
        .get(newUrl)
        .then((response) => {
          this.result_data = response.data
          var optionData = this.getResponseData(response.data)
          this.getEchartData(optionData)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  methods: {
    getResponseData (resData) {
      var dict = {'1970': 1,
        '1971': 2,
        '1972': 3,
        '1973': 4,
        '1974': 5,
        '1975': 6,
        '1976': 7,
        '1977': 8,
        '1978': 9,
        '1979': 10,
        '1980': 11,
        '1981': 12,
        '1982': 13,
        '1983': 14,
        '1984': 15,
        '1985': 16,
        '1986': 17,
        '1987': 18,
        '1988': 19,
        '1989': 20,
        '1990': 21,
        '1991': 22,
        '1992': 23,
        '1993': 24,
        '1994': 25,
        '1995': 26,
        '1996': 27,
        '1997': 28,
        '1998': 29,
        '1999': 30,
        '2000': 31,
        '2001': 32,
        '2002': 33,
        '2003': 34,
        '2004': 35,
        '2005': 36,
        '2006': 37,
        '2007': 38,
        '2008': 39,
        '2009': 40,
        '2010': 41,
        '2011': 42,
        '2012': 43,
        '2013': 44,
        '2014': 45,
        '2015': 46,
        '2016': 47,
        '2017': 48,
        '2020': 49,
        '2025': 50,
        '2030': 51,
        '2035': 52,
        '2040': 53,
        '2045': 54,
        '2050': 55,
        '2055': 56,
        '2060': 57,
        '2065': 58,
        '2070': 59,
        '2075': 60,
        '2080': 61,
        '2085': 62,
        '2090': 63,
        '2095': 64,
        '2100': 65}
      var allyearList = ['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2020', '2025', '2030', '2035', '2040', '2045', '2050', '2055', '2060', '2065', '2070', '2075', '2080', '2085', '2090', '2095', '2100']
      var yearList = allyearList.slice(dict[this.startyear] - 1, dict[this.endyear])
      var respData = this.result_data.body
      var jsonData = {}
      var regions = []
      var seriesObjList = []
      jsonData['title'] = respData[0].indicatorname
      for (var row in respData) {
        var regionCountry = respData[row].region + '(' + respData[row].country_cnt + ')'
        if (respData[row].region === '') {
          regionCountry = 'other' + '(' + respData[row].country_cnt + ')'
        }
        regions.push(regionCountry)
        var seriesObj = {}
        var seriesObjData = []
        seriesObj['name'] = regionCountry
        seriesObj['type'] = 'line'
        // seriesObj['stack'] = 'Total'
        for (var y in yearList) {
          if (respData[row].sum === 7) {
            seriesObjData.push(respData[row]['sum_' + yearList[y]])
          } else if (respData[row].ave === 7) {
            seriesObjData.push(respData[row]['avg_' + yearList[y]])
          }
        }
        seriesObj['data'] = seriesObjData
        seriesObjList.push(seriesObj)
      }
      jsonData['legend'] = regions
      jsonData['category'] = yearList
      jsonData['series'] = seriesObjList
      return jsonData
    },
    getEchartData (optionData) {
      if (optionData == null) {
        optionData = {}
        optionData['title'] = 'Stacked Line'
        optionData['legend'] = ['an example']
        optionData['category'] = ['x1', 'x2', 'x3', 'x4', 'x5']
        optionData['series'] = [
          {
            name: 'an example',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90]
          }
        ]
      }
      var chartDom = document.getElementById('main')
      var myChart = echarts.init(chartDom)

      var option
      option = {
        title: {
          text: optionData.title
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          orient: 'vertical',
          right: 100,
          data: optionData.legend
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          show: true,
          feature: {
            magicType: { type: ['line', 'bar'] }
          },
          saveAsImage: {
            show: true,
            title: 'save as image',
            type: 'png',
            lang: ['click to save']
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: optionData.category
        },
        yAxis: {
          type: 'value'
        },
        series: optionData.series
      }
      option && myChart.setOption(option, true)
    }
  },
  watch: {
    selectIndicatorcode (newValue, oldValue) {
      if (newValue === '') {
        var oldreqUrl = url + '?indicatorcode=' + oldValue
        console.log(oldreqUrl)
        axios
          .get(oldreqUrl)
          .then((response) => {
            this.result_data = response.data
            var optionData = this.getResponseData(response.data)
            this.getEchartData(optionData)
          })
          .catch(function (error) {
            console.log(error)
          })
      } else {
        var reqUrl = url + '?indicatorcode=' + newValue
        console.log(reqUrl)
        axios
          .get(reqUrl)
          .then((response) => {
            this.result_data = response.data
            var optionData = this.getResponseData(response.data)
            this.getEchartData(optionData)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  }
}

// watch two variables: although it is tested useful, to simplify the qestion, this time only calculate sum value, so this is not used now
// computed: {
//   listenChange () {
//     const {selectIndicatorcode, aveSum} = this
//     return {selectIndicatorcode, aveSum}
//   }
// },

// watch: {
//   listenChange (newVal, oldVal) {
//     console.log(`new:${newVal}, old:${oldVal}`)
//     // alert(oldVal.selectIndicatorcode)
//     // alert(oldVal.aveSum)
//     if (newVal.selectIndicatorcode === '' & newVal.aveSum === '') {
//       var oldreqUrl = url + '?indicatorcode=' + oldVal.selectIndicatorcode + '&cal=' + oldVal.aveSum
//       axios
//         .get(oldreqUrl)
//         .then((response) => {
//           this.result_data = response.data
//           var optionData = this.getResponseData(response.data)
//           this.getEchartData(optionData)
//         })
//         .catch(function (error) {
//           console.log(error)
//         })
//     } else if (newVal.selectIndicatorcode === '' & newVal.aveSum !== '') {
//       var reqUrl1 = url + '?indicatorcode=' + oldVal.selectIndicatorcode + '&cal=' + newVal.aveSum
//       alert(reqUrl1)
//       console.log(reqUrl1)
//       axios
//         .get(reqUrl1)
//         .then((response) => {
//           this.result_data = response.data
//           var optionData = this.getResponseData(response.data)
//           this.getEchartData(optionData)
//         })
//         .catch(function (error) {
//           console.log(error)
//         })
//     } else if (newVal.selectIndicatorcode !== '' & newVal.aveSum === '') {
//       var reqUrl2 = url + '?indicatorcode=' + newVal.selectIndicatorcode + '&cal=' + oldVal.aveSum
//       alert(reqUrl2)
//       console.log(reqUrl2)
//       axios
//         .get(reqUrl2)
//         .then((response) => {
//           this.result_data = response.data
//           var optionData = this.getResponseData(response.data)
//           this.getEchartData(optionData)
//         })
//         .catch(function (error) {
//           console.log(error)
//         })
//     } else if (newVal.selectIndicatorcode !== '' & newVal.aveSum !== '') {
//       var reqUrl3 = url + '?indicatorcode=' + newVal.selectIndicatorcode + '&cal=' + newVal.aveSum
//       alert(reqUrl3)
//       console.log(reqUrl3)
//       axios
//         .get(reqUrl3)
//         .then((response) => {
//           this.result_data = response.data
//           var optionData = this.getResponseData(response.data)
//           this.getEchartData(optionData)
//         })
//         .catch(function (error) {
//           console.log(error)
//         })
//     }
//   }
// }
</script>

<style>
</style>
