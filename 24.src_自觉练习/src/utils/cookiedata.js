export function clearAllCookie() {
		var keys = document.cookie.match(/[^ =;]+(?==)/g);
		if(keys) {
			for(var i = keys.length; i--;)
				document.cookie = keys[i] + '=0;expires=' + new Date(0).toUTCString()
		}
	}

export function setCookie(key, value,exdays=30) {
        //校验Key, key中不能有等号【=】
        if(key.indexOf("=") !== -1) {
            throw new Error("Cookie不支持key中使用等号【=】, key:" + key)
        }
        let exdate = new Date() // 获取时间
        exdate.setTime(exdate.getTime() + 24 * 60 * 60 * 1000 * exdays) // 保存的天数
        // 字符串拼接cookie
        // eslint-disable-next-line camelcase
        window.document.cookie = key + '=' + value + ';path=/;expires=' + exdate.toGMTString()
    }

export function getCookie(key) {
        if (document.cookie.length > 0) {
            // 这里显示的格式需要切割一下自己可输出看下
            var arr = document.cookie.split('; ')
            for (let i = 0; i < arr.length; i++) {
                let arr2 = arr[i].split('=') // 再次切割
                // 判断查找相对应的值
                if (arr2[0] === key) {
                    var value = arr2[1];
                    for (let j = 2; j < arr2.length; j++) {
                        value += '=' + arr2[j];
                    }
                    return value;
                }
            }
        }
    }