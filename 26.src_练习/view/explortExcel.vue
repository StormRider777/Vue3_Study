<template>
    <div style="height:500px;overflow: auto">
    <h2>表格数据导出EXCEL</h2>
    <hr>
    <div style="width: 100%;height: 50px">
        <el-button color="red" @click="exportExcel()">
            <el-icon color="#030303" size="18px"><DocumentCopy /></el-icon>
            导出EXCEL
        </el-button>
    </div>
    <el-table :data="tableData.viewdata"
              height="500"
              :highlight-current-row="true"
              border
              id="outtable"
    >
        <el-table-column prop="id" label="ID" width="180"/>
        <el-table-column prop="name" label="姓名" width="180"/>
        <el-table-column prop="salary" label="战力" width="200"/>
        <el-table-column
                prop="tag"
                label="Tag"
                width="100"
                :filters="[
                            { text: '牛逼人', value: '50000' },
                            { text: '衰逼', value: '0' },
                          ]"
                filter-placement="bottom-end"
        >
            <!--:filter-method="filterTag"-->
            <template #default="scope">
                <el-tag
                        :type="scope.row.salary >= 50000 ? 'warning' : 'success'"
                        disable-transitions
                >{{ scope.row.salary >= 50000 ? '牛逼人' : '衰逼' }}
                </el-tag
                >
            </template>
        </el-table-column>
        <el-table-column label="操作">
            <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
                >Edit
                </el-button
                >
                <el-button
                        size="small"
                        type="danger"
                        @click="handleDelete(scope.$index, scope.row)"
                >Delete
                </el-button
                >
            </template>
        </el-table-column>

    </el-table>
    <el-pagination style="margin-top: 10px"
                   v-model:current-page="page.currentPage"
                   v-model:page-size="page.pageSize"
                   :page-sizes="[3,10, 20, 30, 100]"
                   :small="false"
                   :disabled="false"
                   :background="true"
                   :pager-count="5"
                   layout="total, sizes, prev, pager, next, jumper"
                   :total="tableData.data.length"
                   @size-change="handleSizeChange"
                   @current-change="handleCurrentChange"
    />
    </div>
</template>

<script>
    import {onMounted,reactive} from 'vue'
    import axios from 'axios'
    //xlsx 与 file-saver依赖
    //npm install --save xlsx file-saver
    import {ElMessage} from 'element-plus'
    import FileSaver from "file-saver";
    import * as XLSX from "xlsx";

    export default {
        name: "explortExcel",
        setup(){
            const tableData=reactive({
                data:[],
                viewdata:[]
            })
            const page=reactive({
                currentPage:1,
                pageSize:10
            })
            onMounted(()=>{
                axios({
                    method:'get',
                    url:'/dataserver/app01/getalldata/'
                }).then(res=>{
                    tableData.data=res.data
                    handleCurrentChange(1)
                })
            })
            let handleCurrentChange=(number)=>{
                tableData.viewdata=tableData.data.slice((number-1)*page.pageSize,number*page.pageSize)
            }
            let handleSizeChange=(number)=>{
                tableData.viewdata=tableData.data.slice((page.currentPage-1)*page.pageSize,page.currentPage*page.pageSize)
            }

            let exportExcel = () => {
                /* generate workbook object from table */
                var xlsxParam = { raw: true }
                let el=document.querySelector('#outtable')
                if (!el){
                    ElMessage('获取表格元素出现错误')
                    return false
                }
                var wb = XLSX.utils.table_to_book(el,xlsxParam)

                /* get binary string as output */
                var wbout = XLSX.write(wb, {bookType: 'xlsx', bookSST: true, type: 'array'})
                try {
                    FileSaver.saveAs(new Blob([wbout], {type: 'application/octet-stream'}), 'demo.xlsx')
                    ElMessage({message:'成功导出!',type:'success'})
                } catch (e) {
                    if (typeof console !== 'undefined') console.log(e, wbout)
                }
            }
            let handleDelete=(index,row)=>{
                ElMessage({
                    message:`这是<strong style="color:red"> 删除 </strong>按钮!<strong style="color:red">${row.name}</strong>`,
                    type:'warning',
                    dangerouslyUseHTMLString:true
                })
                console.log(index,row)
            }
            let handleEdit=(index,row)=>{
                ElMessage({
                    message:`这是<strong style="color:red"> 编辑 </strong>按钮!<strong style="color:red">${row.name}</strong>`,
                    type:'info',
                    dangerouslyUseHTMLString:true
                })
                console.log(index,row)
            }
            return {tableData,handleSizeChange,handleCurrentChange,page,exportExcel,handleDelete,handleEdit}
        }
    }

    function openLocalFile(fileName) {
        try {
            var obj = new ActiveXObject("WScript.shell");
            if (obj) {
                obj.run("'" + fileName + "'");
                obj = null;
            }
        } catch (e) {
            alert('路径文件不存在/请在IE浏览器访问打开/组件未注册');
        }
    }

    // 调用函数

</script>

<style scoped>

</style>