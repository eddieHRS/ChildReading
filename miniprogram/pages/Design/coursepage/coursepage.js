// pages/coursepage/coursepage.js
Page({
  data: {
    Title: '单课标题示例',
    VideoUrl: '',
    Ques: []
  },

  onLoad : function (e) {
    var type = e.type
    var id = e.id
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:5000/studypage',
      method: "GET",
      data: {
          type: type,
          id :id
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success: function (res) {
        that.setData({
          Title: res.data.data.title,
          VideoUrl: res.data.data.vedioUrl,
          Ques: res.data.data.ques
        })
      }
    })
  },
  changestage: function(e){
    var that = this;
    var num = e.currentTarget.dataset.num;
    console.log(num);
    wx.request({
      url: 'http://127.0.0.1:5000/changestage',
      data: {
        num:num
      },
      method: 'GET',
      success: function(res){
        console.log(res);
        that.load();
      }
    })
  },
  // 上传图片
  doUpload: function () {
    // 选择图片
    wx.chooseImage({
      count: 1,
      sizeType: ['compressed'],
      sourceType: ['album', 'camera'],
      success: function (res) {

        wx.showLoading({
          title: '上传中',
        })

        const filePath = res.tempFilePaths[0]

        // 上传图片
        const cloudPath = 'my-image' + filePath.match(/\.[^.]+?$/)[0]
        wx.cloud.uploadFile({
          cloudPath,
          filePath,
          success: res => {
            console.log('[上传文件] 成功：', res)

            app.globalData.fileID = res.fileID
            app.globalData.cloudPath = cloudPath
            app.globalData.imagePath = filePath

            wx.navigateTo({
              url: '../storageConsole/storageConsole'
            })
          },
          fail: e => {
            console.error('[上传文件] 失败：', e)
            wx.showToast({
              icon: 'none',
              title: '上传失败',
            })
          },
          complete: () => {
            wx.hideLoading()
          }
        })

      },
      fail: e => {
        console.error(e)
      }
    })
  },
})