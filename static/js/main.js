//trim ltrim rtrim


String.prototype.trim=function(){
　    return this.replace(/(^\s*)|(\s*$)/g, "");
　 }

String.prototype.ltrim=function(){
　    return this.replace(/(^\s*)/g,"");
　 }

String.prototype.rtrim=function(){
　    return this.replace(/(\s*$)/g,"");
　 }

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

function removeCookie(cname) {
    setCookie(cname,"",1);
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}

function isPhoneNumberValidate(phoneNumber) {
    var pattern =/^(0|86|17951)?(13[0-9]|15[012356789]|17[0-9]|18[0-9]|14[57])[0-9]{8}$/;
    if (pattern.test(phoneNumber)) {
        return true;
    }
    return false;
}

// 检查电话是否是座机
function checkPhoneIsLandLine(phoneNumber) {
    var pattern = /^[0-9]{8}$/;
    if (pattern.test(phoneNumber)) {
        return true;
    }
    return false;
}

function isValidAddress(address) {
    //    if "路" not in address and "弄" not in address and "号" not in address and "巷" not in address and "道" not in address:
    var pattern = /.*?(路|弄|号|巷|道).*?/;
    if(pattern.test(address)) {
        return true;
    }
    return false;
}

function isEmailValidate(email) {
    var pattern = /^.+\@.+\..+$/;
    if (pattern.test(email)) {
        return true;
    }
    return false;
}

