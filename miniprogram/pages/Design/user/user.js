// pages/user/user.js
const app = getApp()

Page({
  data: {
  //用户头像昵称信息
    avatarUrl: './user-unlogin.png',
    userInfo: {},
    logged: false,
    takeSession: false,
    requestResult: '',
    credits: 0,
    ranks: 0,
  
  },

  onLoad: function () {
    if (!wx.cloud) {
      wx.redirectTo({
        url: '../chooseLib/chooseLib',
      })
      return
    }
    wx.login({
      success: function (res){
        console.log('asasdas');
        console.log(res.code);
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              this.setData({
                avatarUrl: res.userInfo.avatarUrl,
                userInfo: res.userInfo
              })
            }
          })
        }
      }
    })


    //交互
    var that = this
    wx.request({
      url: 'http://127.0.0.1:5000/user',
      method: "GET",
      data: {
        //stu_id
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success: function(res) {
        that.setData({
          credits: res.data.data.credits,
          ranks: res.data.data.ranks
        })
      }
    })
  },

  onGetUserInfo: function (e) {
    if (!this.logged && e.detail.userInfo) {
      this.setData({
        logged: true,
        avatarUrl: e.detail.userInfo.avatarUrl,
        userInfo: e.detail.userInfo
      })
    }
  },
  
  goToQuery: function () {
    wx.navigateTo({
      url: '../query/query'
    });
  },

})
