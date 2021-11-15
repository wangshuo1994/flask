<template>
  <el-container>
    <el-aside width="200px">
      <p>Please input the filter</p>
      <tr>
        <td width="180">
          <el-input
            v-model="indicatorcode"
            placeholder="indicatorcode"></el-input>
        </td>
      </tr>
      <tr>
        <el-select v-model="select_indicatorcode" placeholder="please select">
          <el-option
            v-for="item in options1"
            :key="item.value"
            :label="item.label"
            :value="item.value"{">"}
          </el-option>
        </el-select>
      </tr>
       <tr>
        <el-select v-model="ave_sum" placeholder="please choose ave/sum">
          <el-option
            v-for="item in options2"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </tr>
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
      indicatorcode: '',
      startyear: '',
      endyear: '',
      showdata: true,
      options1: [{
        value: 'UIS.SAP.CE.F',
        label: 'Population of compulsory school age, female (number)'
      }, {
        value: 'UIS.LP.AG15T99',
        label: 'Adult illiterate population, 15+ years, both sexes (number)'
      }, {
        value: '选项3',
        label: '蚵仔煎'
      }, {
        value: '选项4',
        label: '龙须面'
      }, {
        value: '选项5',
        label: '北京烤鸭'
      }],
      select_indicatorcode: '',
      options2: [{
        value: 'ave',
        label: 'Calculate average value'
      }, {
        value: 'sum',
        label: 'Calculate sum value'
      }],
      ave_sum: ''
    }
  },
  mounted () {
    axios
      .get(url)
      .then((response) => (this.result_data = response.data))
      .catch(function (error) {
        console.log(error)
      })
    this.getEchartData()
  },
  methods: {
    getResponseData (resData) {
      var yearList = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2009', '2010']
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
        seriesObj['stack'] = 'Total'
        for (var y in yearList) {
          seriesObjData.push(respData[row]['sum_' + yearList[y]])
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
    indicatorcode (newValue, oldValue) {
      if (newValue === '') {
        var oldreqUrl = url + '?indicatorcode=' + oldValue + '&cal=' + this.ave_sum
        alert(oldreqUrl)
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
        var reqUrl = url + '?indicatorcode=' + newValue + '&cal=' + this.ave_sum
        alert(reqUrl)
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
    },
    select_indicatorcode (newValue, oldValue) {
      if (newValue === '') {
        var oldreqUrl = url + '?indicatorcode=' + oldValue + '&cal=' + this.ave_sum
        alert(oldreqUrl)
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
        var reqUrl = url + '?indicatorcode=' + newValue + '&cal=' + this.ave_sum
        alert(reqUrl)
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
    },
    ave_sum (newValue, oldValue) {
      if (newValue === '') {
        var oldreqUrl = url + '?indicatorcode=' + this.indicatorcode + '&cal=' + oldValue
        alert(oldreqUrl)
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
        var reqUrl = url + '?indicatorcode=' + this.indicatorcode + '&cal=' + newValue
        alert(reqUrl)
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
</script>

<style>
</style>
