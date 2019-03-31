var titleList = ['阅读写作课', '阅读绘画课', '成长阅读课']

Page({
  data:{
//标题
  index: 1,

//更新:显示套课课程
  set_id: 1,
  set_classList: ['《七只瞎老鼠》','《拼拼凑凑的变色龙》','《你很特别》','《黎明》','《迟到大王》'],
  set_teacher : '叶凤春',

  },
  onLoad: function () {
    var that = this
    wx.request({
      url: '',
      method: "POST",
      data: {
        'func_id': 0,

      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success: function (res) {
        that.setData({
          set_classList: res.data.set_classList,
          set_teacher: res.data.set_teacher,
        })
      }
    })
    wx.getStorage({
      key: 'jumpIndex',
      success: function (res) {
        //console.log(res)
        var i = res.data-6
        wx.setNavigationBarTitle({
          title: titleList[i],
        })
        that.setData({ 
          index: i, 
          set_id: i
          })
      }
    })
    //支付
    wx.requestPayment(
      {
        'timeStamp': '',
        'nonceStr': '',
        'package': '',
        'signType': 'MD5',
        'paySign': '',
        'success': function (res) { },
        'fail': function (res) { },
        'complete': function (res) { }
      })
  },
  pay: function() {
    
  }
})
