var app = getApp();
Page({
  data:{
  set_title: '',
  set_classList: ['《七只瞎老鼠》','《拼拼凑凑的变色龙》','《你很特别》','《黎明》','《迟到大王》'],
  set_banji: [] //开设的班级

  },
  onLoad: function (e) {
    var that = this
    wx.request({
      url: 'http://127.0.0.1:5000/buyset',
      method: "GET",
      data: {
        //sid:套课的id
        sid: e.scourse
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success: function (res) {
        that.setData({
          set_title: res.data.data.set_title,
          set_classList: res.data.data.set_classList,
          set_banji: res.data.data.set_banji,
        })
      }
    })
  },
  //支付并且把课程加入到已选课表中
  payandadd: function(e) {
    console.log("需要支付的class_id", e.currentTarget.dataset.class_id)
    console.log("openid", app.globalData.openid)
    wx.request({
      url: 'http://127.0.0.1:5000/payandadd',
      data: {
        class_id: e.currentTarget.dataset.class_id,
        open_id: app.globalData.openid
      },
      method: 'GET',
      success: function(res){
        console.log(res)
        wx.showToast({
          title: '套课加入成功',
          icon: 'success',
          duration: 2000//持续的时间
        })
      }
    })
  },


})
