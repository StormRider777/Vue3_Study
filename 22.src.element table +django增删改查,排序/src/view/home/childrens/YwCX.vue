<template>
    <div>
        <div style="width: 100%;height: 50px;line-height: 50px">
        <el-input v-model="tableData.querykw" style="width:400px;height: 35px;margin-left: 15px">

        </el-input>
        <el-button @click="querydata" type="success" style="width: 150px;height: 35px;margin-left: 20px">
            <el-icon>
                <Search/>
            </el-icon>
            查询
        </el-button>
    </div>
        <el-table :data="tableData.data.slice((Page.currentPage-1)*Page.pagesize,(Page.currentPage-1)*Page.pagesize+Page.pagesize)"
              border highlight-current-row
              :row-style="{height:'35px'}"
              :header-cell-style="{height:'35px',background:'darkgray','text-align':'center',color:'snow'}"
              :cell-style="rowcolor"
              :default-sort="{prop:'name',order:'order'}"
              height="540" style="width: 100%"
              @row-dblclick="handleEditrow">
        <el-table-column prop="id" label="ID" width="60"/>
        <el-table-column prop="name" label="姓名" width="100"  :show-overflow-tooltip="true" :sortable="true" />
        <el-table-column prop="cardid" label="证件号码" width="180"  :show-overflow-tooltip="true" />
        <el-table-column prop="tele" label="电话" width="130"  :show-overflow-tooltip="true"  :sortable="true" />
        <el-table-column prop="gzdw" label="工作单位" :show-overflow-tooltip="true" />
        <el-table-column label="操作">
            <template #default="scope">
                <el-button type='primary' @click="handleEdit(scope.$index, scope.row,scope)" style="width: 60px;height: 25px">
                    <el-icon> <Edit/></el-icon>修改
                </el-button>
                <el-button type="danger" @click="handleDelete(scope.$index, scope.row)" style="width: 60px;height: 25px">
                    <el-icon><Delete /></el-icon>删除
                </el-button>
            </template>
        </el-table-column>
    </el-table>

        <el-pagination
          v-model:current-page="Page.currentPage"
          v-model:page-size="Page.pagesize"
          :page-sizes="[10,20,50,100]"
          :small="Page.small"
          :disabled="Page.disabled"
          :background="Page.background"
          layout="sizes, prev, pager, next, jumper,->,total "
          :total="Page.total"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :hide-on-single-page="false"
          prev-text="上一页"
          next-text="下一页"
          total-text="总记录数:"
          style="margin: 10px auto"
        />
        <el-dialog v-model="dialogupdatedata" title="修改数据" :close-on-click-modal="false">
            <table width="100%" class="updateformtable">
                <tr><td class="fieldlabel">姓名:</td><td><el-input v-model="updateform.name" autocomplete="off" /></td></tr>
                <tr><td  class="fieldlabel">证件号码:</td><td><el-input v-model="updateform.cardid" autocomplete="off" /></td></tr>
                <tr><td  class="fieldlabel">电话:</td><td><el-input v-model="updateform.tele" autocomplete="off" /></td></tr>
                <tr><td  class="fieldlabel">工作单位:</td><td><el-input v-model="updateform.gzdw" autocomplete="off" /></td></tr>
            </table>


            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogupdatedata = false">取消修改</el-button>
                    <el-button type="primary" @click="updaterow">
                    确定修改
                    </el-button>
                </span>
            </template>


        </el-dialog>
    </div>
</template>

<script>
    import {ref,reactive,onMounted} from 'vue'
    import axios from "axios"
    import {ElMessageBox,ElDialog} from 'element-plus'
    export default {
        name: "YwCX",
        setup(){
            const dialogupdatedata=ref(false)
            const Page=reactive({
                currentPage: 1,
                pagesize:10,
                small:false,
                background:true,
                disabled:false,
                total:0,
            })
            const updateform=reactive({
                id:'',
                name:'',
                cardid:'',
                tele:'',
                gzdw:'',
            })
            const handleSizeChange = (val) => {
              Page.pagesize=val
            }
            const handleCurrentChange = (val) => {
                //console.log((Page.currentPage-1)*Page.pagesize,Page.pagesize)
                Page.currentPage=val
            }

            const tableData=reactive({data:[],querykw:'',currentrow:null})
            onMounted(()=>{
                axios({
                    url:"/dataserver/data/getyzdata/",
                    method:'get',
                    params:{}
                }).then((res)=>{
                    let s=res.data
                    s.forEach((r)=>{
                        Page.total++
                        tableData.data.push(r)
                    })

                }).catch((err)=>{
                    tableData.data.push({name:'发生错误',cardid:err.code,tele:err.name,gzdw:err.message})
                })
            })
            function rowcolor(row){
                if (row.row.name==='发生错误' && row.columnIndex<=2){
                    return {color:'red'}
                }
            }
            const updaterow=()=>{
                dialogupdatedata.value=false
                let data={
                    id:updateform.id,
                    name:updateform.name,
                    tele:updateform.tele,
                    gzdw:updateform.gzdw,
                    cardid:updateform.cardid
                }
                axios({
                    url:`/dataserver/data/getyzdata/`,
                    method:'post',
                    data,
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                }).then(res=>{
                    let data=res.data.data

                    for (let i=0;i<=tableData.data.length;i++){
                        let r=tableData.data[i]
                        if (r.id===parseInt(data.id)){
                            r.name=data.name
                            r.tele=data.tele
                            r.cardid=data.cardid
                            r.gzdw=data.gzdw
                            break
                        }
                    }
                    ElMessageBox.alert(res.data.msg,'提示',{type:'success'})
                }).catch(err=>{
                    console.log(err.message)
                })
            }
            const querydata=()=>{
                tableData.data.splice(0,tableData.data.length)
                Page.total=0

                axios({
                    url:`/dataserver/data/getyzdata/?querykw=${tableData.querykw}`,
                    method:'get',
                    params:{}
                }).then((res)=>{
                    let s=res.data
                    s.forEach((r)=>{
                        Page.total++
                        tableData.data.push(r)
                    })
                }).catch((err)=>{
                    tableData.data.push({name:'发生错误',cardid:err.code,tele:err.name,gzdw:err.message})
                })
            }
            const handleDelete=(index,row)=>{
                ElMessageBox.confirm(
                        `确认删记录:<strong style="margin-left:10px;color:red"> ${row.name} ${row.cardid}</strong>`,
                        '请确定是否删除',
                        {
                            dangerouslyUseHTMLString:true,
                            confirmButtonText:'删除',
                            cancelButtonText:'取消',
                            closeOnPressEscape:true,
                            closeOnClickModal:false,
                            type:'warning'
                        }
                    ).then(res=>{
                        axios({
                            url:`/dataserver/data/getyzdata/`,
                            method:'post',
                            data:{type:'dele',id:row.id},
                            headers: {
                                'Content-Type': 'application/x-www-form-urlencoded'
                            },
                        }).then(res=>{
                            let r=(Page.currentPage-1)*Page.pagesize+index
                            tableData.data.splice(r,1)
                            ElMessageBox.alert(
                                `删除了:<strong style="color: red"> ${ row.name } ${ row.cardid } </strong>`,'提示',
                                {
                                    dangerouslyUseHTMLString:true,
                                    confirmButtonText:'确定',
                                    closeOnClickModal:false,
                                    type:'warning'
                                })
                        }).catch(err=>{
                            console.log('失败了:',err.message)
                        })
                    }
                )
            }
            const handleEdit=(index,row,s)=>{
                // let r=(Page.currentPage-1)*Page.pagesize+index
                // tableData.data[r]['name']=Math.ceil(Math.random()*1000000)
                // tableData.data[r]['gzdw']=Math.ceil(Math.random()*1000000)
                //console.log(index,row,s)
                dialogupdatedata.value=!dialogupdatedata.value
                updateform.name=row.name
                updateform.tele=row.tele
                updateform.gzdw=row.gzdw
                updateform.cardid=row.cardid
                updateform.id=row.id

            }
            const handleEditrow=(row,col)=>{
                handleEdit(0,row)
            }
            return {updateform,tableData,rowcolor,Page,handleSizeChange,
                    handleCurrentChange,querydata,handleEdit,handleDelete,
                    dialogupdatedata,handleEditrow,updaterow}

        }
    }

</script>

<style>
    .el-table--enable-row-hover .el-table__body tr:hover>td{
        background: skyblue !important;
        color: yellow;
    }
    .current-row>td{
        background: darkblue !important;
        color: yellow;
    }
    .updateformtable>tr{
        height: 45px;
    }
    .fieldlabel{
        text-align: right;
        width:100px;
    }
</style>