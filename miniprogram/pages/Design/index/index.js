//index.js
const app = getApp()
Page({
  data: {
//滚动相关
    swiperCurrent: 0,
    indicatorDots: true,
    autoplay: true,
    interval: 6000,
    duration: 800,
    circular: true,
    beforeColor: "rgba(255,255,255,.3)",
    afterColor: "coral",
    imgUrls: [
      'https://i.loli.net/2019/03/18/5c8ee04809c12.jpg',
      'https://i.loli.net/2019/03/18/5c8ee09ca123c.jpg',
      'https://i.loli.net/2019/03/18/5c8ee0b1bfda9.jpg'
    ],
    links: [
      '../user/user',
      '../user/user',
      '../user/user'
    ],
//跳转相关  
    jumpList: ['11', '12', '13', '21', '22', '23', '31', '32', '33'],



  },
  
  onLoad : function () {
    var that = this
    wx.request({
      url: '',
      method: "POST",
      data: {
        'func_id': 1
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success:function(res) {
        that.setData({
          imgUrls:res.data.imgUrls,
          pageImgUrls:res.data.pageImgUrls,
          courseTitle:res.data.courseTitle,
          courseIntro:res.data.courseIntro,
          courseLinks:res.data.courseLinks
        })
      }
    })
  },


  //轮播图的切换事件
  swiperChange: function (e) {
    this.setData({
      swiperCurrent: e.detail.current
    })
  },
  //点击指示点切换
  chuangEvent: function (e) {
    this.setData({
      swiperCurrent: e.currentTarget.id
    })
  },
  //点击图片触发事件
  swipclick: function (e) {
    console.log(this.data.swiperCurrent);
    wx.switchTab({
      url: this.data.links[this.data.swiperCurrent]
    })
  },

  onLoad: function() {
    if (!wx.cloud) {
      wx.redirectTo({
        url: '../chooseLib/chooseLib',
      })
      return
    }  
  },

  //跳转+传值
  clickjump: function(e) {
    var that = this;
    var tmp = e.currentTarget.dataset.value;
    //app.globalData.jumpIndex = tmp;
    //console.log(app.globalData.jumpIndex)
    wx.setStorageSync('jumpIndex', tmp)
    wx.navigateTo({
      url: '../department/department',
    })
  },
  clickjump2: function (e) {
    var that = this;
    var tmp = e.currentTarget.dataset.value;
    //app.globalData.jumpIndex = tmp;
    //console.log(app.globalData.jumpIndex)
    wx.setStorageSync('jumpIndex', tmp)
    wx.navigateTo({
      url: '../buyset/buyset',
    })
  }
})
