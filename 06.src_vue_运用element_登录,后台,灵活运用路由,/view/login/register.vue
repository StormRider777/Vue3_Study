<template>
    <div style="width: 750px;height: 550px;border: 1px solid grey;margin: 20px auto;padding: 10px 10px 10px 10px;border-radius: 3px ">
        <h4 style="color:red">用户注册</h4>
        <hr>
        <el-form :model="form" label-width="120px">
            <el-form-item label="姓名:">
                <el-input v-model="form.name" placeholder="请输入姓名..." clearable />
            </el-form-item>
            <el-form-item label="文化程度:">
                <el-select v-model="form.region" placeholder="选择学历..." style="width: 100%">
                    <el-option label="博士" value="boshi" />
                    <el-option label="硕士" value="shuoshi" />
                    <el-option label="本科" value="benke" />
                    <el-option label="大专" value="dazhuan" />
                </el-select>
            </el-form-item>
            <el-form-item label="时间:">
                <el-col :span="12">
                    <el-date-picker
                      v-model="form.date1"
                      type="date"
                      :editable="false"
                      placeholder="起始日期.."
                      style="width: 100%"/>
                </el-col>
                <el-col :span="1" class="text-center">
                    <span class="text-gray-500" style="margin-left: 10px ">-</span>
                </el-col>
                <el-col :span="11">
                    <el-time-picker
                      v-model="form.date2"
                      placeholder="时间.."
                      style="width: 100%"
                      :editable="false"
                    />
                </el-col>
            </el-form-item>
            <el-form-item label="VIP用户:">
                <el-switch v-model="form.vip" />
            </el-form-item>
            <el-form-item label="爱好:">
                <el-checkbox-group v-model="form.hobby">
                    <el-checkbox label="抽烟" name="type" />
                    <el-checkbox label="喝酒" name="type" />
                    <el-checkbox label="烫头" name="type" />
                    <el-checkbox label="打游戏" name="type" />
                </el-checkbox-group>
            </el-form-item>
            <el-form-item label="性别:">
                <el-radio-group v-model="form.sex">
                    <el-radio label="男" />
                    <el-radio label="女" />
                </el-radio-group>
            </el-form-item>
            <el-form-item label="其他信息:">
                <el-input v-model="form.desc" type="textarea" placeholder="请输入其他信息...." :rows='3' resize="none" maxlength="30" show-word-limit/>
            </el-form-item>
            <el-form-item style="margin: 35px auto">
                <el-button type="primary" @click="onSubmit()" style="width: 80%;height: 40px" :icon="Edit">提交注册</el-button>
            </el-form-item>
        </el-form>

    </div>
</template>

<script>
    import { Edit } from '@element-plus/icons-vue'
    import {reactive} from 'vue'
    export default {
        name: "Register",
        setup(){
            const form = reactive({
                name: '',
                degree: '',
                date1: '',
                date2: '',
                vip: false,
                hobby: [],
                sex: '',
                desc: '',
            })
            function onSubmit() {
                console.log(form)
            }
            return {form,Edit,onSubmit}
        }
    }
</script>

<style scoped>

</style>