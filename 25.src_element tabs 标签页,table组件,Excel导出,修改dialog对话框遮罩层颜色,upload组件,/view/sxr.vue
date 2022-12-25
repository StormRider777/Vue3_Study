<template>
    <el-button @click="DialogVisible=!DialogVisible" >确认</el-button>
    <div style="margin: 200px auto;width:900px">
        <el-input value="赵磊" width="400px"></el-input>
        <br>
        <el-input value="23213421432134234" width="400px"></el-input>
        <br>
        <el-input value="18553875317" width="400px"></el-input>
    </div>
    <el-dialog
            v-model="DialogVisible"
            width="400px"
            align-center
    >
        <table>
            <tr><td>失信被执行人姓名 : 赵磊</td></tr>
            <tr><td>失信被执行人身份证号码 :52365655600012474</td></tr>
            <tr><td>51X</td></tr>
            <tr><td>执行法院 : 肥城市人民法院</td></tr>
            <tr><td>执行依据文号 : (2022)鲁1209民初0892号</td></tr>
            <tr><td>作出执行依据单位 : 肥城市人民法院</td></tr>
        </table>

    </el-dialog>

    <!--
    遮罩层 .el-dialog__wrapper 颜色 :#5A5A5A 字体 #F69200
    -->
</template>

<script>
    import {ref} from 'vue'
    export default {
        name: "sxr",
        setup(){
            const DialogVisible=ref(false)

            return {DialogVisible}

        }

    }
</script>

<style>
    tr{
        height: 25px;
    }
td{
    color:#F69200;

}
.el-overlay{
        background:rgba(188,88,88,0.5) ;
    }
</style>