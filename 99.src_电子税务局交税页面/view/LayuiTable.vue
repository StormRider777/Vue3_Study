<template>
  <!--<lay-button @click="changeSelectedKeys">修改选中</lay-button>-->
  <!--<lay-button @click="changeDataSource23">修改数据</lay-button>-->
  <lay-table :columns="columns"
             :data-source="dataSource.data"
            >

  </lay-table>
</template>

<script>
import { ref ,reactive} from 'vue'

export default {
    name: "LayuiTable",
    setup() {

    const selectedKeys5 = ref(["1","3"]);

    const getCheckboxProps = (data,index) => {
      if(index == 2) {
        return {disabled: true}
      }
      return {};
    }

    // const changeSelectedKeys = () => {
    //   selectedKeys5.value = ["2"]
    // }

    // const changeDataSource23 = () => {
    //   dataSource23.value = [
    //     {id:"1",username:"root", password:"root",sex:"男", age:"18", remark: 'layui - vue（谐音：类 UI) '},
    //     {id:"2",username:"root", password:"root",sex:"男", age:"18", remark: 'layui - vue（谐音：类 UI) '}
    //   ]
    // }

    const columns = [
        // {
        //   type: "checkbox",
        // },
        // {
        //   title:"序号",
        //   width: "50px",
        //   key:'xh',
        //   align:'center'
        // },
        // {
        //   title:"应征凭证序号",
        //   width: "200px",
        //   key:"pzxh",
        //   align:'center'
        // },
      {
        type: "checkbox",
      },
      {
        title:"账户",
        width:"200px",
        key:"username",
        fixed: "left"
      },{
        title:"密码",
        width: "300px",
        key:"xh"
      },{
        title:"性别",
        key:"pzxh"
      }
      // ,{
      //   title:"年龄",
      //   width: "300px",
      //   key:"age"
      // },
      // {
      //   title:"备注",
      //   width: "180px",
      //   key:"remark",
      //   ellipsisTooltip: true
      // }
    ]

    const dataSource23 = [
      {
        id:"1",
        pzxh:"10013721000081741920",
    },
    {
        id:"2",
        pzxh:"10013722000002160890",
    },
    {
        id:"3",
        pzxh:"10013722000028429871",
    },
      /*
      {id:"1",username:"root", password:"root",sex:"男", age:"18", remark: 'layui - vue（谐音：类 UI) '},
      {id:"2",username:"root", password:"root",sex:"男", age:"18", remark: 'layui - vue（谐音：类 UI) '},
      {id:"3",username:"woow", password:"woow",sex:"男", age:"20", remark: 'layui - vue（谐音：类 UI) '},
      {id:"4",username:"woow", password:"woow",sex:"男", age:"20", remark: 'layui - vue（谐音：类 UI) '},
      {id:"5",username:"woow", password:"woow",sex:"男", age:"20", remark: 'layui - vue（谐音：类 UI) '}
      */
    ]

      // const columns23 =[
      //           {
      //               type: "checkbox",
      //           },
      //           {
      //               title:"序号",
      //               width: "50px",
      //               key:'xh',
      //               align:'center'
      //           },
      //           {
      //               title:"应征凭证序号",
      //               width: "200px",
      //               key:"pzxh",
      //               align:'center'
      //           },
      //           {
      //               title:"税（费）种",
      //               width: "150px",
      //               key:"sfz",
      //           },
      //           {
      //               title:"税（品）种",
      //               width: "200px",
      //               key:"spz",
      //           },
      //           {
      //               title:"税款所属起",
      //               width: "130px",
      //               key:"skqdate",
      //               align:'center'
      //           },
      //           {
      //               title:"税款所属止",
      //               width: "130px",
      //               key:"skzdate",
      //               align:'center'
      //           },
      //           {
      //               title: "缴款期限",
      //               width: "130px",
      //               key: "jkqx",
      //               align:'center'
      //           },
      //           {
      //               title: "应补退税额",
      //               width: "120px",
      //               key: "ybtsk",
      //               align:'right'
      //
      //           },
      //           {
      //               title: "实缴金额",
      //               width: "200px",
      //               key: "sjje",
      //               align:'right'
      //            },
      //           {
      //               title: "滞纳金",
      //               width: "100px",
      //               key: "znj",
      //               align:'right'
      //           },
      //           {
      //               title: "是否逾期",
      //               width: "80px",
      //               key: "sfyq",
      //               align:'center'
      //           }
      //       ]
      // const dataSource23 =[
      //     {
      //         xh:"1",
      //         pzxh:"10013721000081741920",
      //         sfz: '城镇土地使用税',
      //         spz:'建制镇土地使用税等级1',
      //         skqdate:'2021-07-01',
      //         skzdate:'2021-09-30',
      //         jkqx:'2021-10-26',
      //         ybtsk:'800.00',
      //         sjje:'800.00',
      //         znj:'0.00',
      //         sfyq:'是'
      //     },
      //     {
      //         xh:"2",
      //         pzxh:"10013722000002160890",
      //         sfz: '城镇土地使用税',
      //         spz:'建制镇土地使用税等级1',
      //         skqdate:'2021-10-01',
      //         skzdate:'2021-12-31',
      //         jkqx:'2022-01-19',
      //         ybtsk:'800.00',
      //         sjje:'800.00',
      //         znj:'0.00',
      //         sfyq:'是'
      //     },
      //     {
      //         xh:"3",
      //         pzxh:"10013722000028429871",
      //         sfz: '城镇土地使用税',
      //         spz:'建制镇土地使用税等级1',
      //         skqdate:'2022-01-01',
      //         skzdate:'2022-03-31',
      //         jkqx:'2022-04-20',
      //         ybtsk:'800.00',
      //         sjje:'800.00',
      //         znj:'0.00',
      //         sfyq:'是'
      //     },
      //     {
      //         xh:"4",
      //         pzxh:"10013722000050606999",
      //         sfz: '城镇土地使用税',
      //         spz:'建制镇土地使用税等级1',
      //         skqdate:'2022-04-01',
      //         skzdate:'2022-06-30',
      //         jkqx:'2022-07-15',
      //         ybtsk:'800.00',
      //         sjje:'800.00',
      //         znj:'0.00',
      //         sfyq:'是'
      //     },
      //     {
      //         xh:"5",
      //         pzxh:"10013722000079231705",
      //         sfz: '城镇土地使用税',
      //         spz:'建制镇土地使用税等级1',
      //         skqdate:'2022-07-01',
      //         skzdate:'2022-09-30',
      //         jkqx:'2022-10-25',
      //         ybtsk:'800.00',
      //         sjje:'800.00',
      //         znj:'0.00',
      //         sfyq:'是'
      //     },
      // ]

    const dataSource=reactive({
        data:dataSource23
    })

    return {
      columns,
      dataSource,
      // selectedKeys5,
      // changeSelectedKeys,
      // getCheckboxProps,
      // changeDataSource23
    }
  }
}
</script>

<style>

    .layui-form-checked[lay-skin=primary] i{
        border-color: #0994dc;
        background-color: #0994dc;
        color: #fff;
    }
    .layui-icon{
        border-color: #0994dc;
    }

    .layui-table thead th{
        text-align: center;
    }
    .layui-laypage .layui-laypage-count,.layui-laypage .layui-laypage-skip {
        font-size: 14px;
    }
    .layui-laypage select{
        margin-top: 0;
        height: 30px;
        font-size: 14px;
    }
    .layui-btn-normal{
        height: 45px;
        width: 115px;
        font-size: 16px;
    }
    .layui-btn-warm{
        height: 45px;
        width: 205px;
        font-size: 16px;
    }
</style>