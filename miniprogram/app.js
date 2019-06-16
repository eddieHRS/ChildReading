//app.js
App({
  globalData: {
    openid: '1111'
  },
  
  onLaunch: function () {
    
  },

  onLaunch: function(){
    var that = this
    wx.login({
      success: function (res) {
        wx.request({
          url: 'http://127.0.0.1:5000/openid',
          method: 'GET',
          data: {
            code: res.code
          },
          success: function (e) {
            that.globalData.openid = e.data.openid
            console.log(that.globalData.openid)
          }
        })

      }
    })
  },
  // onShow: function(){
  //   console.log(this.globalData.openid)
  // }
})