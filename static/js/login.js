<script>  
function validateform(){  
var reg=document.myform.reg.value;  
var name=document.myform.name.value;  
var password=document.myform.password.value; 
if (reg==null || reg.length!=12){  
  alert("Provide Valid Register Number");  
  return false;  
  }  
if (name==null || name==""){  
  alert("Name can't be blank");  
  return false;  
}
else if(password.length<6){  
  alert("Password must be at least 6 characters long.");  
  return false;  
  }  
 return(true); 
}  
</script>  
