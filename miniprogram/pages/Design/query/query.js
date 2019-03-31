 // pages/Design/query/query.js
Page({
  data: {
    checkboxArr: [{ checked: false, name: '一年级' }, { checked: false, name: '二年级' }, { checked: false, name: '三年级' }, { checked: false, name: '四年级' }, { checked: false, name: '五年级' }, { checked: false, name: '六年级' }],
    checkboxArr2: [{ checked: false, name: '一' }, { checked: false, name: '二' }, { checked: false, name: '三' }, { checked: false, name: '四' }, { checked: false, name: '五' }, { checked: false, name: '六' }],
    checkboxArr3: [{ checked: false, name: 'A' }, { checked: false, name: 'B' }, { checked: false, name: 'C' }, { checked: false, name: 'D' }],

  isFirst: false,

//信息收集
  garde: 4,
  gender: 'unknowngender',
  age: 10,
  name: 'unknownname',
  city: 'unknowncity',
  //问卷结果
  answer_booksHaveRead: ['', ...''],
  answer_singleChoice: ['', ...''],
  answer_booksFavorite:'',
  }, 

  onLoad : function () {
    var that = this
    wx.request({
      url: '',
      method: "POST",
      data: {
        'stu_id' : stu_id,
        'grade': grade,
        'gender': gender,
        'age': age,
        'name': name,
        'city': city,
        'answer_booksHaveRead': answer_booksHaveRead,
        'answer_singleChoice': answer_singleChoice,
        'answer_booksFavorite': answer_booksFavorite
      },
      header: { 'Content_Type': 'application/x-www-form-urlencoded' },
      success: function (res) {
        that.setData({ 
          test: res.data 
        });
        console.log(res.data)  
      }
    })
  },


  nameInput: function(e) {
    this.setData ({
      name: e.detail.value
    })
  }, 
  ageInput: function (e) {
    this.setData({
      age: e.detail.value
    })
  }, 
  genderInput: function (e) {
    this.setData({
      gender: e.detail.value
    })
  }, 
  cityInput: function (e) {
    this.setData({
      city: e.detail.value
    })
  }, 
  booksInput: function (e) {
    this.setData({
      answer_booksFavorite: e.detail.value
    })
  }, 

  checkbox: function (e) {
    var index = e.currentTarget.dataset.index;//获取当前点击的下标
    var checkboxArr2 = this.data.checkboxArr2;//选项集合    
    checkboxArr2[index].checked = !checkboxArr2[index].checked;//改变当前选中的checked值    
    this.setData({      
      checkboxArr2: checkboxArr2    
      });  
    },  
  checkboxChange: function (e) {    
    var checkValue = e.detail.value;    
    this.setData({      
      checkValue: checkValue    
      });  
    },

  radio: function (e) {
  var index = e.currentTarget.dataset.index;//获取当前点击的下标
  var checkboxArr = this.data.checkboxArr;//选项集合
  if(checkboxArr[index].checked) return;//如果点击的当前已选中则返回
  checkboxArr.forEach(item => {
      item.checked = false
    })
  checkboxArr[index].checked = true;//改变当前选中的checked值
  this.setData({
     checkboxArr: checkboxArr
    });
  },
  radioChange: function (e) {
    var checkValue = e.detail.value;
    this.setData({
      checkValue: checkValue
    });
  },

  radio3: function (e) {
    var index = e.currentTarget.dataset.index;//获取当前点击的下标
    var checkboxArr3 = this.data.checkboxArr3;//选项集合
    if (checkboxArr3[index].checked) return;//如果点击的当前已选中则返回
    checkboxArr3.forEach(item => {
      item.checked = false
    })
    checkboxArr3[index].checked = true;//改变当前选中的checked值
    this.setData({
      checkboxArr3: checkboxArr3
    });
  },
  radioChange3: function (e) {
    var checkValue = e.detail.value;
    this.setData({
      checkValue: checkValue
    });
  },

  confirm: function () {// 提交
    console.log(this.data.checkValue, this.data.checkboxArr2, this.data.checkboxArr3);//所有选中的项的value

    //待完善推荐算法 应跳转到推荐课程列表
    wx.redirectTo({
      url: '../recomd/recomd'
    });
  },
})