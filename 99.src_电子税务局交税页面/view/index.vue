<template>
    <div style="padding: 10px 10px 10px 15px;">
        <table width="100%" >
            <tbody>
                <tr style="height: 50px">
                    <td style="width: 46px;padding: 8px"><img src="../assets/1.png" alt="" style="height: 50px;width: 50px"></td>
                    <td style="text-align: left;padding: 8px"><div style="font-size: 28px">税费缴纳</div></td>
                </tr>
            </tbody>
        </table>
        <lay-table
                id="xh"
                :columns="columnsdata"
                :data-source="dataSource.data"
                :row="selectRow()"
                v-model:selectedKeys="selectedKeys"
                >
            <!--:getCheckboxProps="getCheckboxProps"-->
        </lay-table>

        <lay-page v-model="page.current" v-model:limit="page.limit"
                  :total="page.total"
                  :limits="page.limits"
                  :show-count="true" :show-page="true" :show-limit="true" :show-refresh="false"  theme="blue"
                  :showSkip="true" @change="change"></lay-page>

        <ul class="layui-row site-doc-color site-doc-necolor"  style="font-size: 14px">
            <li class="layui-col-md24" style="line-height: 65px">
                <div style="background-color: #f6f6f6;;margin: 5px auto;height: 65px;text-align: right;padding-right: 5px">
                    <lay-checkbox name="like" skin="primary"  v-model="checkall" value="1" label="是否一并缴纳滞纳金"></lay-checkbox>
                    <span v-html="result" style="font-size: 16px"></span>
                </div>
            </li>
        </ul>

        <div style="width: 100%;margin: 10px auto;display: flex;justify-content: left;align-items: center">
            <div style="width: 5px;background: #22B6E7;border-radius: 5px;height: 25px"></div>
            <div style="font-size: 20px;margin-left: 5px">缴款方式</div>
        </div>
        <div style="padding-top:15px;line-height: 90px;display: flex;justify-content: left;align-items: center">
            <div style="width: 197px;height: 70px;border: 1px solid #ddd;display: flex;justify-content: center;align-items: center">
                <a href="javascript:void(0)"><img src="../assets/2.jpg" alt="" style="width: 175px;height: 48px"></a>
            </div>
            <div style="margin-left:20px;width: 197px;height: 70px;border: 1px solid #ddd;display: flex;justify-content: center;align-items: center">
                <a href="javascript:void(0)"><img src="../assets/3.jpg" alt="" style="width: 175px;height: 48px"></a>
            </div>
            <div style="margin-left:20px;width: 197px;height: 70px;border: 1px solid #ddd;display: flex;justify-content: center;align-items: center">
                <a href="javascript:void(0)"><img src="../assets/4.jpg" alt="" style="width: 175px;height: 48px"></a>
            </div>
        </div>
        <div class="layui-col-md24" style="line-height: 74px;margin-top: 50px">
            <div style="height: 74px;text-align: center">
                <lay-button type="normal">立即缴款</lay-button>
                <lay-button type="warm" style="margin-left: 30px">未缴款凭证作废(解锁)</lay-button>
            </div>
        </div>

    </div>
</template>

<script>
    import {reactive,ref,onMounted} from 'vue'
    export default {
        name: "index",
        setup(){
            const columnsdata =[
                {
                    type: "checkbox",
                    align:'center'
                },
                {
                    title:"序号",
                    width: "50px",
                    key:'xh',
                    align:'center',
                },
                {
                    title:"应征凭证序号",
                    width: "200px",
                    key:"pzxh",
                    align:'center',
                },
                {
                    title:"税（费）种",
                    width: "150px",
                    key:"sfz",
                },
                {
                    title:"税（品）种",
                    width: "200px",
                    key:"spz",
                },
                {
                    title:"税款所属起",
                    width: "130px",
                    key:"skqdate",
                    align:'center',
                },
                {
                    title:"税款所属止",
                    width: "130px",
                    key:"skzdate",
                    align:'center',
                },
                {
                    title: "缴款期限",
                    width: "130px",
                    key: "jkqx",
                    align:'center'
                },
                {
                    title: "应补退税额",
                    width: "120px",
                    key: "ybtsk",
                    align:'right',
                },
                {
                    title: "实缴金额",
                    width: "200px",
                    key: "sjje",
                    align:'right',
                 },
                {
                    title: "滞纳金",
                    width: "100px",
                    key: "znj",
                    align:'right',
                },
                {
                    title: "是否逾期",
                    width: "80px",
                    key: "sfyq",
                    align:'center'
                }
            ]
            const data =reactive([
                {
                    xh:"1",
                    pzxh:"10013721000060422371",
                    sfz: '城镇土地使用税',
                    spz:'建制镇土地使用税等级1',
                    skqdate:'2021-04-01',
                    skzdate:'2021-06-30',
                    jkqx:'2021-07-15',
                    ybtsk:formatPrice(800),
                    sjje:formatPrice(800),
                    znj:formatPrice(0),
                    sfyq:'是'
                },
                {
                    xh:"2",
                    pzxh:"10013721000081741920",
                    sfz: '城镇土地使用税',
                    spz:'建制镇土地使用税等级1',
                    skqdate:'2021-07-01',
                    skzdate:'2021-09-30',
                    jkqx:'2021-10-26',
                    ybtsk:formatPrice(800),
                    sjje:formatPrice(800),
                    znj:formatPrice(0),
                    sfyq:'是'
                },
                {
                    xh:"3",
                    pzxh:"10013722000002160890",
                    sfz: '城镇土地使用税',
                    spz:'建制镇土地使用税等级1',
                    skqdate:'2021-10-01',
                    skzdate:'2021-12-31',
                    jkqx:'2022-01-19',
                    ybtsk:formatPrice(800),
                    sjje:formatPrice(800),
                    znj:formatPrice(0),
                    sfyq:'是'
                },
                {
                    xh:"4",
                    pzxh:"10013722000028429871",
                    sfz: '城镇土地使用税',
                    spz:'建制镇土地使用税等级1',
                    skqdate:'2022-01-01',
                    skzdate:'2022-03-31',
                    jkqx:'2022-04-20',
                    ybtsk:formatPrice(800),
                    sjje:formatPrice(800),
                    znj:formatPrice(0),
                    sfyq:'是'
                },
                {
                    xh:"5",
                    pzxh:"10013722000050606999",
                    sfz: '城镇土地使用税',
                    spz:'建制镇土地使用税等级1',
                    skqdate:'2022-04-01',
                    skzdate:'2022-06-30',
                    jkqx:'2022-07-15',
                    ybtsk:formatPrice(800),
                    sjje:formatPrice(800),
                    znj:formatPrice(0),
                    sfyq:'是'
                },
                {
                    xh:"6",
                    pzxh:"10013722000079231705",
                    sfz: '城镇土地使用税',
                    spz:'建制镇土地使用税等级1',
                    skqdate:'2022-07-01',
                    skzdate:'2022-09-30',
                    jkqx:'2022-10-25',
                    ybtsk:formatPrice(800),
                    sjje:formatPrice(800),
                    znj:formatPrice(0),
                    sfyq:'是'
                },
            ])
            const selectedKeys=ref([])
            const page=reactive({
                total: 0,
                limit: 10,
                limits:[5,10,20,30,40,50],
                current: 1,
                showPage:true,
                showSkip:true,
                showCount:true,
                //pages:0
                //pages:2,
                //showRefresh: true,
            })
            const dataSource=reactive({
                data:data.slice(0,page.limit)
                //data:data
            })

            page.total=data.length
            const change=({current, limit})=>{
                dataSource.data=data.slice((current-1)*limit,(current-1)*limit+limit)
            }
            var msjje
            onMounted(()=>{
                for (var r in data){
                    msjje=data[r].sjje.replace(',','')
                    //console.log(msjje)
                    data[r].znj=formatPrice(jsznj(parseFloat(msjje),data[r].jkqx))
                }
            })

            let skje=''
            let znjje=''
            let totalje=''

            const result=ref(``)

            const checkall=ref(true)
            let selectRow=()=>{

                let rows=dataSource.data
                var sumskje=0
                var sumznj=0
                var j=0
                var mskje,mznj
                // console.log(selectedKeys.value)
                for (var i in selectedKeys.value){
                    //console.log(rows[selectedKeys.value[i]-1])
                    mskje=rows[selectedKeys.value[i]-1].sjje.replace(',','')
                    mznj=rows[selectedKeys.value[i]-1].znj.replace(',','')
                    sumskje=sumskje+parseFloat(mskje)
                    sumznj=sumznj+parseFloat(mznj)
                    jsznj(rows[selectedKeys.value[i]-1].sjje,rows[selectedKeys.value[i]-1].jkqx)
                    j=j+1
                }

                totalje=formatPrice(sumznj+sumskje)
                znjje=formatPrice(sumznj)
                skje=formatPrice(sumskje)
                //console.log(totalje,sumznj,skje,znjje)

                result.value=`共选择
                        <strong>${j}</strong>条待清缴记录。
                        实缴金额<strong style="color: #0994dc">${skje}</strong>元，
                        滞纳金<strong style="color: #0994dc">${znjje}</strong>元，
                        合计<strong style="color:red;font-size: 28px">${totalje}</strong>元。`
            }
            return {
                checkall,
                result,
                page,
                change,
                columnsdata,
                dataSource,
                selectedKeys,
                selectRow,
            }
        }
    }
    function formatPrice(number) {
      return number.toLocaleString('zh-CN', {minimumFractionDigits: 2,useGrouping: true})
    }
    function jsznj(skje,qsdate) {
        let today=new Date()
        let qsr=new Date(qsdate)
        let diffdate=today-Date.parse(qsr)
        let znj=skje*(Math.ceil(diffdate/(1000*3600*24)))*(15/10000)
        // console.log(skje,qsdate,znj)
        return znj
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