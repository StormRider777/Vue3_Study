<template>
   <div style="width: 100%">
        <h3 style="color: slateblue;margin-left: 20px">业务输入</h3>
        <hr>
        <el-container>
            <table style="width: 50%;margin-right: 20px">
                <tr><td style="width: 110px;text-align: right">姓名:</td><td><el-input v-model="data.name" placeholder="请输入..." clearable></el-input></td></tr>
                <tr><td style="width: 110px;text-align: right">证件号码:</td><td><el-input v-model="data.cardid" placeholder="请输入..." clearable></el-input></td></tr>
                <tr><td style="width: 110px;text-align: right">联系电话:</td><td><el-input v-model="data.tele" placeholder="请输入..." clearable></el-input></td></tr>
                <tr><td style="width: 110px;text-align: right">工作地址:</td>
                    <td>
                        <el-select v-model="data.gzdw" placeholder="请选择..." style="width: 100%">
                            <el-option value="上海">上海</el-option>
                            <el-option value="北京">北京</el-option>
                            <el-option value="广州">广州</el-option>
                            <el-option value="深圳">深圳</el-option>
                            <el-option value="新疆">新疆</el-option>
                            <el-option value="山东">山东</el-option>
                        </el-select>
                    </td>
                </tr>
                <tr><td style="width: 110px;text-align: right">爱好:</td>
                    <td>
                        <el-checkbox-group v-model="data.hobby" :min="1" :max="3">
                            <el-checkbox label="抽烟" />
                            <el-checkbox label="收钱"  />
                            <el-checkbox label="仓库发货" />
                            <el-checkbox label="复核"  />
                        </el-checkbox-group>
                    </td>
                </tr>
                <tr><td style="width: 110px;text-align: right">性别:</td>
                    <td >
                        <el-radio-group v-model="data.sex">
                            <el-radio label="官员" />
                            <el-radio label="百姓" />
                        </el-radio-group>
                    </td>
                </tr>
                <tr style="height: 100px">
                    <td colspan="2" style="text-align: center">
                        <el-button style="width: 80%;height: 40px" type="success" @click="submitbtn">
                            <el-icon style="color:red"><Select /></el-icon>
                            保存并增加下一个
                        </el-button>
                    </td>
                </tr>
            </table>
        </el-container>
    </div>
</template>

<script>
    import {reactive} from 'vue'
    import axios from 'axios'
    import {ElMessageBox} from 'element-plus'
    export default {
        name: "YzGL",
        setup(){
            const data=reactive({
                name:'',
                cardid:'',
                tele:'',
                gzdw:'',
                hobby:[],
                sex:'',
            })
            const submitbtn=()=>{
                axios({
                    url:`/dataserver/data/getyzdata/`,
                    method:'post',
                    data:{type:'add',
                            name:data.name,
                            cardid:data.cardid,
                            tele:data.tele,
                            gzdw:data.tele,
                            hobby:data.hobby.join(','),
                            sex:data.sex
                    },
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                }).then(res=>{
                    //console.log(res.data)
                    ElMessageBox.alert(res.data.msg+' <strong style="color:red">'+res.data.data.name+"</strong>",'提示',{
                        type:'success',
                        dangerouslyUseHTMLString:true
                    }).then(r=>{
                        data.gzdw=''
                        data.name=''
                        data.tele=''
                        data.cardid=''
                        data.hobby=[]
                        data.sex=''
                    })
                })
            }
            return {data,submitbtn}
        }
    }
</script>

<style scoped>
tr{
    height: 45px;
}
td{
    margin-left: 20px;
}
.el-checkbox__input.is-checked .el-checkbox__inner, .el-checkbox__input.is-indeterminate .el-checkbox__inner{
  background-color:#990000;
  border-color: #000099;
}
.el-checkbox__input.is-checked , .el-checkbox__label {
  color: #000099;
}
.el-checkbox.is-bordered.is-checked{
  border-color: #000099;
}
.el-checkbox__input.is-focus .el-checkbox__inner{
  border-color:  #000099;
}
.el-checkbox__label{
    font-size: 16px;
}

</style>