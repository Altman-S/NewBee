(function(e){function t(t){for(var n,o,i=t[0],s=t[1],l=t[2],h=0,b=[];h<i.length;h++)o=i[h],Object.prototype.hasOwnProperty.call(r,o)&&r[o]&&b.push(r[o][0]),r[o]=0;for(n in s)Object.prototype.hasOwnProperty.call(s,n)&&(e[n]=s[n]);u&&u(t);while(b.length)b.shift()();return a.push.apply(a,l||[]),c()}function c(){for(var e,t=0;t<a.length;t++){for(var c=a[t],n=!0,i=1;i<c.length;i++){var s=c[i];0!==r[s]&&(n=!1)}n&&(a.splice(t--,1),e=o(o.s=c[0]))}return e}var n={},r={app:0},a=[];function o(t){if(n[t])return n[t].exports;var c=n[t]={i:t,l:!1,exports:{}};return e[t].call(c.exports,c,c.exports,o),c.l=!0,c.exports}o.m=e,o.c=n,o.d=function(e,t,c){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:c})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var c=Object.create(null);if(o.r(c),Object.defineProperty(c,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)o.d(c,n,function(t){return e[t]}.bind(null,n));return c},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],s=i.push.bind(i);i.push=t,i=i.slice();for(var l=0;l<i.length;l++)t(i[l]);var u=s;a.push([0,"chunk-vendors"]),c()})({0:function(e,t,c){e.exports=c("56d7")},"153a":function(e,t,c){"use strict";c("25d6")},"25d6":function(e,t,c){},"2e61":function(e,t,c){},"313c":function(e,t,c){},3856:function(e,t,c){},"56d7":function(e,t,c){"use strict";c.r(t);c("e260"),c("e6cf"),c("cca6"),c("a79d");var n=c("7a23");function r(e,t,c,r,a,o){var i=Object(n["F"])("router-view");return Object(n["y"])(),Object(n["e"])(i)}var a={name:"App",components:{},data:function(){return{}}},o=(c("6859"),c("6b0d")),i=c.n(o);const s=i()(a,[["render",r]]);var l=s,u=c("6c02"),h=(c("07ac"),c("b0c0"),c("8491")),b=c.n(h),j=function(e){return Object(n["B"])("data-v-3963aba2"),e=e(),Object(n["z"])(),e},d={class:"home"},O={class:"header"},v={class:"logo"},p=["href"],f=j((function(){return Object(n["h"])("img",{src:b.a,width:"150",height:"112",alt:""},null,-1)})),m=[f],g={key:0,class:"result"};function y(e,t,c,r,a,o){var i=Object(n["F"])("router-link"),s=Object(n["F"])("search-bar"),l=Object(n["F"])("router-view");return Object(n["y"])(),Object(n["g"])("div",d,[Object(n["h"])("div",O,[Object(n["h"])("div",v,[Object(n["j"])(i,{to:"/",custom:""},{default:Object(n["M"])((function(e){var t=e.href;return[Object(n["h"])("a",{href:t},m,8,p)]})),_:1})]),Object(n["j"])(s)]),Object(n["h"])("div",{class:Object(n["s"])({resultpage:"/search"==this.$route.path||"/searchAll"==this.$route.path,infopage:"/search"!=this.$route.path&&"/searchAll"!=this.$route.path})},["/search"==this.$route.path||"/searchAll"==this.$route.path?(Object(n["y"])(),Object(n["g"])("h3",g," Results for '"+Object(n["I"])(Object.values(this.$route.query)[0])+"' ",1)):Object(n["f"])("",!0),Object(n["h"])("div",{class:Object(n["s"])({container:"/search"==this.$route.path||"/searchAll"==this.$route.path})},[Object(n["j"])(l,null,{default:Object(n["M"])((function(e){var t=e.Component,c=e.route;return[(Object(n["y"])(),Object(n["e"])(n["b"],null,[c.meta.keepAlive?(Object(n["y"])(),Object(n["e"])(Object(n["G"])(t),{key:c.name})):Object(n["f"])("",!0)],1024)),c.meta.keepAlive?Object(n["f"])("",!0):(Object(n["y"])(),Object(n["e"])(Object(n["G"])(t),{key:c.name}))]})),_:1})],2)],2)])}c("ac1f"),c("841c");var _=function(e){return Object(n["B"])("data-v-2cf3d8bc"),e=e(),Object(n["z"])(),e},w={class:"container d-flex justify-content-center"},k={class:"input-group mb-3"},I={class:"dropdown"},x={class:"btn btn-secondary dropdown-toggle",type:"button",id:"dropdownMenuButton1","data-bs-toggle":"dropdown","aria-expanded":"false"},P={class:"dropdown-menu","aria-labelledby":"dropdownMenuButton1"},A=["onClick"],M={class:"list-group"},T=["onClick"],C={class:"input-group-append"},D=_((function(){return Object(n["h"])("i",{class:"fas fa-search"},null,-1)})),$=[D];function F(e,t,c,r,a,o){return Object(n["y"])(),Object(n["g"])("div",{class:Object(n["s"])({startPage:"Start Page"==this.$parent.$options.name,homePage:"Home"==this.$parent.$options.name})},[Object(n["h"])("div",w,[Object(n["h"])("div",k,[Object(n["h"])("div",I,[Object(n["h"])("button",x,Object(n["I"])(e.searchFilter),1),Object(n["h"])("ul",P,[(Object(n["y"])(!0),Object(n["g"])(n["a"],null,Object(n["E"])(e.filter_list,(function(e){return Object(n["y"])(),Object(n["g"])("li",null,[Object(n["h"])("button",{class:"dropdown-item",onClick:function(t){return o.changeFilter(e)}},Object(n["I"])(e),9,A)])})),256))])]),Object(n["N"])(Object(n["h"])("input",{type:"text",class:"form-control",id:"searchBar",placeholder:"search","onUpdate:modelValue":t[0]||(t[0]=function(t){return e.searchText=t}),onKeydown:t[1]||(t[1]=Object(n["O"])((function(){return o.search&&o.search.apply(o,arguments)}),["enter"])),onKeyup:t[2]||(t[2]=function(e){return o.get(e)})},null,544),[[n["K"],e.searchText]]),Object(n["h"])("ul",M,[(Object(n["y"])(!0),Object(n["g"])(n["a"],null,Object(n["E"])(e.myData,(function(e){return Object(n["y"])(),Object(n["g"])("li",{class:"list-group-item",onClick:function(t){return o.caa(e)}},Object(n["I"])(e),9,T)})),256))]),Object(n["h"])("div",C,[Object(n["h"])("button",{class:"btn btn-primary",onClick:t[3]||(t[3]=function(){return o.search&&o.search.apply(o,arguments)})},$)])])])],2)}var N=c("ade3"),S=c("1da1"),q=(c("498a"),c("d3b7"),c("99af"),c("96cf"),c("25a0")),B=c("e3e1");c("4d63"),c("c607"),c("2c3e"),c("25f0"),c("00b4");function R(e){var t=new RegExp(/^(19[5-9]\d|20[0-4]\d|2050)$/);return t.test(e.trim())}var E={name:"Search Bar",data:function(){return{api:"api/movies/check",v$:Object(q["a"])(),searchText:"",searchFilter:"All",filter_list:["All","Title","Year","Genre","Celebrity"],myData:[],tt:"",now:-1}},methods:{caa:function(e){this.searchText=e},search:function(){var e=this;return Object(S["a"])(regeneratorRuntime.mark((function t(){var c;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return"/home/search?"+e.searchFilter+"="+e.searchText,t.next=3,e.v$.$validate();case 3:c=t.sent,0==c?alert("Wrong input"):"All"==e.searchFilter?(console.log("search All"),e.$router.push({path:"/searchAll",query:Object(N["a"])({},e.searchFilter,e.searchText)})):(console.log("search category"),e.$router.push({path:"/search",query:Object(N["a"])({},e.searchFilter,e.searchText)}));case 5:case"end":return t.stop()}}),t)})))()},changeFilter:function(e){this.searchFilter=e,this.searchText=""},get:function(e){38!==e.keyCode&&40!==e.keyCode&&(this.myData=[],this.throttle(this.getData,window))},getData:function(){var e=this;this.searchText=this.searchText.trim(),fetch("".concat(this.api,"?input=").concat(this.searchText)).then((function(e){return e.json()})).then((function(t){"success"==t.response&&(e.myData=t.promp)}))},throttle:function(e,t){clearTimeout(e.tId),e.tId=setTimeout((function(){e.call(t)}),1e3)}},validations:function(){switch(this.searchFilter){case"All":return{searchText:{required:B["a"]}};case"Title":return{searchText:{required:B["a"]}};case"Genre":return{searchText:{required:B["a"]}};case"Celebrity":return{searchText:{required:B["a"]}};case"Year":return{searchText:{required:B["a"],validate_year:R}}}}};c("a1d9");const G=i()(E,[["render",F],["__scopeId","data-v-2cf3d8bc"]]);var K=G,U={name:"Home",components:{SearchBar:K}};c("8197");const Y=i()(U,[["render",y],["__scopeId","data-v-3963aba2"]]);var z=Y,L={class:"title"},V={class:"box"},H={class:"left"},J=["src","alt"],W={class:"info"},Q={class:"director"},X={class:"actors"},Z={class:"gerne"},ee={class:"rating"},te={class:"votes"},ce={class:"runtime"},ne={class:"imdbid"},re={class:"plot-title"};function ae(e,t,c,r,a,o){return Object(n["y"])(),Object(n["g"])(n["a"],null,[Object(n["h"])("h1",L,Object(n["I"])(e.movie.Title)+" ("+Object(n["I"])(e.movie.Year)+")",1),Object(n["h"])("div",V,[Object(n["h"])("div",H,[Object(n["h"])("img",{src:e.movie.Poster,class:"img-fluid rounded-start",alt:e.movie.Title},null,8,J)]),Object(n["h"])("div",W,[Object(n["h"])("div",Q,"Director: "+Object(n["I"])(e.movie.Director),1),Object(n["h"])("div",X,"Actors: "+Object(n["I"])(e.movie.Actors),1),Object(n["h"])("div",Z,"Gerne: "+Object(n["I"])(e.movie.Genre),1),Object(n["h"])("div",ee,"Rating: "+Object(n["I"])(e.movie.imdbRating),1),Object(n["h"])("div",te,"Votes: "+Object(n["I"])(e.movie.imdbVotes),1),Object(n["h"])("div",ce,"Runtime: "+Object(n["I"])(e.movie.Runtime),1),Object(n["h"])("div",ne,"IMDB ID: "+Object(n["I"])(e.movie.imdbID),1),Object(n["h"])("div",null,[Object(n["h"])("h3",re,"Plot of "+Object(n["I"])(e.movie.Title),1),Object(n["h"])("h4",null,Object(n["I"])(e.movie.Plot),1)])])])],64)}var oe={name:"MovieInfoPage",props:{id:String},data:function(){return{api:"/api/movies/id/",movie:Object}},created:function(){var e=this;console.log("MovieInfoPage created");var t=this.id;console.log("".concat(this.api).concat(t)),fetch("".concat(this.api).concat(t)).then((function(e){return e.json()})).then((function(t){"success"==t.response&&(console.log(t.response),e.movie=t.movie)}))}};c("9a14");const ie=i()(oe,[["render",ae]]);var se=ie,le=function(e){return Object(n["B"])("data-v-0efd3270"),e=e(),Object(n["z"])(),e},ue=le((function(){return Object(n["h"])("img",{src:b.a,class:"logo"},null,-1)}));function he(e,t,c,r,a,o){var i=Object(n["F"])("search-bar");return Object(n["y"])(),Object(n["g"])(n["a"],null,[ue,Object(n["j"])(i)],64)}var be={id:"box"};function je(e,t,c,r,a,o){return Object(n["y"])(),Object(n["g"])("div",be,[Object(n["N"])(Object(n["h"])("input",{type:"text","onUpdate:modelValue":t[0]||(t[0]=function(t){return e.tt=t}),name:"",onKeyup:t[1]||(t[1]=function(e){return o.get(e)}),onKeydown:[t[2]||(t[2]=Object(n["O"])((function(e){return o.changeDown()}),["down"])),t[3]||(t[3]=Object(n["O"])((function(e){return o.changeUp()}),["up"]))]},null,544),[[n["K"],e.tt]]),Object(n["h"])("ul",null,[(Object(n["y"])(!0),Object(n["g"])(n["a"],null,Object(n["E"])(e.myData,(function(t,c){return Object(n["y"])(),Object(n["g"])("li",{class:Object(n["s"])({gray:c===e.now})},Object(n["I"])(t),3)})),256))])])}var de={name:"searchBar with dropdown",data:function(){return{myData:[],tt:"",now:-1}},methods:{get:function(e){38!==e.keyCode&&40!==e.keyCode&&(13===e.keyCode&&(window.open("https://www.baidu.com/s?wd="+this.tt),this.tt=""),this.throttle(this.getData,window))},changeDown:function(){this.now++,this.now===this.myData.length&&(this.now=-1),this.tt=this.myData[this.now]},changeUp:function(){this.now--,-2===this.now&&(this.now=this.myData.length-1),this.tt=this.myData[this.now]},getData:function(){},throttle:function(e,t){clearTimeout(e.tId),e.tId=setTimeout((function(){e.call(t)}),300)}}};c("bf15");const Oe=i()(de,[["render",je],["__scopeId","data-v-c07e4f94"]]);var ve=Oe,pe={name:"Start Page",components:{SearchBar:K,Dropdown:ve}};c("cc76");const fe=i()(pe,[["render",he],["__scopeId","data-v-0efd3270"]]);var me=fe,ge=function(e){return Object(n["B"])("data-v-881d5b7a"),e=e(),Object(n["z"])(),e},ye=ge((function(){return Object(n["h"])("div",{class:"content1"},[Object(n["h"])("h1",null,"Sorry, no result for it.")],-1)})),_e=ge((function(){return Object(n["h"])("div",{class:"content2"},[Object(n["h"])("h1",null,"We are working hard to enlarge our database."),Object(n["h"])("h1",null,"Please try another keywords in the searching box."),Object(n["h"])("h1",null,"Thanks for your patience.")],-1)})),we=[ye,_e];function ke(e,t,c,r,a,o){return Object(n["y"])(),Object(n["g"])("div",null,we)}var Ie={name:"ErrorPage"};c("8820");const xe=i()(Ie,[["render",ke],["__scopeId","data-v-881d5b7a"]]);var Pe=xe,Ae={class:"row gy-5"},Me={class:"col-10"};function Te(e,t,c,r,a,o){var i=Object(n["F"])("movie-card-container"),s=Object(n["F"])("pagination");return Object(n["y"])(),Object(n["g"])("div",Ae,[Object(n["h"])("div",Me,[Object(n["j"])(i,{movies:e.movies},null,8,["movies"]),Object(n["j"])(s,{total_page:o.total_page,current_page:e.current_page,onChangePage:t[0]||(t[0]=function(e){return o.change_page(e)})},null,8,["total_page","current_page"])])])}c("b64b"),c("3ca3"),c("ddb0"),c("9861"),c("5319");var Ce={class:"list-group"};function De(e,t,c,r,a,o){var i=Object(n["F"])("movie-card"),s=Object(n["F"])("router-link");return Object(n["y"])(),Object(n["g"])("div",Ce,[(Object(n["y"])(!0),Object(n["g"])(n["a"],null,Object(n["E"])(c.movies,(function(e){return Object(n["y"])(),Object(n["g"])("div",null,[Object(n["j"])(s,{to:"/movie/"+e.imdbID,custom:""},{default:Object(n["M"])((function(t){var c=t.href;return[Object(n["j"])(i,{movie:e,href:c},null,8,["movie","href"])]})),_:2},1032,["to"])])})),256))])}c("1276");var $e={class:"card"},Fe={class:"row"},Ne={class:"col-md-2"},Se=["src","alt"],qe={class:"col-md-10"},Be={class:"card-body"},Re={class:"card-title card-text"},Ee=["href"],Ge={class:"card-text"},Ke={class:"card-text",style:{color:"khaki"}},Ue={class:"card-text",style:{color:"aqua"}},Ye={class:"card-text"};function ze(e,t,c,r,a,o){return Object(n["y"])(),Object(n["g"])("div",$e,[Object(n["h"])("div",Fe,[Object(n["h"])("div",Ne,[Object(n["h"])("img",{src:c.movie.Poster,class:"img-fluid rounded-start",alt:c.movie.Title},null,8,Se)]),Object(n["h"])("div",qe,[Object(n["h"])("div",Be,[Object(n["h"])("h5",Re,[Object(n["h"])("a",{class:"card-text",href:c.href},Object(n["I"])(c.movie.Title),9,Ee),Object(n["h"])("span",null,"("+Object(n["I"])(c.movie.Year)+")",1)]),Object(n["h"])("p",Ge,[Object(n["i"])(Object(n["I"])(c.movie.Runtime?c.movie.Runtime:"N/A")+" ",1),(Object(n["y"])(!0),Object(n["g"])(n["a"],null,Object(n["E"])(c.movie.Genre.split(","),(function(e){return Object(n["y"])(),Object(n["g"])("span",null," | "+Object(n["I"])(e),1)})),256))]),Object(n["h"])("p",Ke," Director: "+Object(n["I"])(c.movie.Director?c.movie.Director:"N/A"),1),Object(n["h"])("p",Ue,[Object(n["i"])(" Actors: "+Object(n["I"])(c.movie.Actors?c.movie.Actors:"N/A")+" ",1),(Object(n["y"])(!0),Object(n["g"])(n["a"],null,Object(n["E"])(c.movie.Actors.split(","),(function(e){return Object(n["y"])(),Object(n["g"])("span",null," | "+Object(n["I"])(e),1)})),256))]),Object(n["h"])("p",Ye,Object(n["I"])("N/A"==c.movie.Plot?"No Plot":c.movie.Plot),1)])])])])}var Le={name:"MovieCard",props:{href:String,movie:Object}};c("6835");const Ve=i()(Le,[["render",ze],["__scopeId","data-v-43fe29ce"]]);var He=Ve,Je={name:"MovieCardContainer",props:{movies:Array},components:{MovieCard:He},data:function(){return{}}};const We=i()(Je,[["render",De]]);var Qe=We,Xe={"aria-label":"Page navigation example"},Ze={class:"pagination justify-content-center"},et={key:0,class:"page-item"},tt=["onClick"],ct={key:1,class:"page-item"};function nt(e,t,c,r,a,o){return Object(n["y"])(),Object(n["g"])("nav",Xe,[Object(n["h"])("ul",Ze,[c.current_page>1?(Object(n["y"])(),Object(n["g"])("li",et,[Object(n["h"])("button",{class:"page-link",onClick:t[0]||(t[0]=function(e){return o.change_page(c.current_page-1)})}," Previous ")])):Object(n["f"])("",!0),(Object(n["y"])(!0),Object(n["g"])(n["a"],null,Object(n["E"])(o.pages,(function(e){return Object(n["y"])(),Object(n["g"])("li",{class:Object(n["s"])(["page-item",{active:c.current_page==e}])},[Object(n["h"])("button",{class:"page-link",onClick:function(t){return o.change_page(e)}},Object(n["I"])(e),9,tt)],2)})),256)),c.current_page<c.total_page?(Object(n["y"])(),Object(n["g"])("li",ct,[Object(n["h"])("button",{class:"page-link",onClick:t[1]||(t[1]=function(e){return o.change_page(c.current_page+1)})}," Next ")])):Object(n["f"])("",!0)])])}c("a9e3");var rt={name:"Pagination",props:{total_page:Number,current_page:{type:Number,default:1,required:!0},maxVisibleButtons:{type:Number,required:!1,default:10},showItem:{type:Number,required:!1,default:5}},methods:{change_page:function(e){this.$emit("changePage",e)}},computed:{pages:function(){var e=[];if(this.current_page<this.showItem){var t=Math.min(this.showItem,this.total_page);while(t)e.unshift(t--)}else{var c=this.current_page-Math.floor(this.showItem/2);t=this.showItem;c>this.total_page-this.showItem&&(c=this.total_page-this.showItem+1);while(t--)e.push(c++)}return e}}};const at=i()(rt,[["render",nt]]);var ot=at,it={name:"MovieListPage",components:{MovieCardContainer:Qe,MovieCard:He,Pagination:ot},created:function(){var e=this;console.log("MovieListPage created"),this.$watch((function(){return e.$route.query}),(function(t,c){e.search_params={};var n=e.$route.query;if(0!=Object.keys(n).length){for(var r in n)e.search_params[r]=n[r];e.search()}}),{immediate:!0})},data:function(){return{api:"/api/movies/search",movies:null,total_number:null,current_page:1,search_params:{},movies_per_page:20}},methods:{change_page:function(e){var t=this;window.scrollTo(0,0),this.search_params["page"]=e;var c=new URLSearchParams(this.search_params);console.log("".concat(this.api,"?").concat(c)),fetch("".concat(this.api,"?").concat(c)).then((function(e){return e.json()})).then((function(e){console.log(e.response);var c=e.movies;console.log(c.length),t.movies=c,t.current_page=e.current_page}))},search:function(){var e=this;if(void 0==this.search_params.All){var t=new URLSearchParams(this.search_params);console.log("".concat(this.api,"?").concat(t)),window.scrollTo(0,0),fetch("".concat(this.api,"?").concat(t)).then((function(e){return e.json()})).then((function(t){"success"==t.response?(e.movies=t.movies,e.total_number=t.total_number,e.current_page=t.current_page):e.$router.replace({path:"/notfound/1"})}))}}},computed:{total_page:function(){return Math.ceil(this.total_number/this.movies_per_page)}}};const st=i()(it,[["render",Te]]);var lt=st,ut=function(e){return Object(n["B"])("data-v-09c8d44e"),e=e(),Object(n["z"])(),e},ht={class:"row gy-5"},bt={class:"col-10"},jt={class:"bg-grey"},dt=ut((function(){return Object(n["h"])("h4",{class:"abc"},"Title",-1)})),Ot={class:"rightright"},vt=ut((function(){return Object(n["h"])("h4",{class:"def"},"More",-1)})),pt={key:1,class:"card",style:{color:"red"}},ft={class:"col-10"},mt={class:"bg-grey"},gt=ut((function(){return Object(n["h"])("h4",{class:"abc"},"Celebrity",-1)})),yt={class:"rightright"},_t=ut((function(){return Object(n["h"])("h4",{class:"def"},"More",-1)})),wt={key:1,class:"card",style:{color:"red"}},kt={class:"col-10"},It={class:"bg-grey"},xt=ut((function(){return Object(n["h"])("h4",{class:"abc"},"Genre",-1)})),Pt={class:"rightright"},At=ut((function(){return Object(n["h"])("h4",{class:"def"},"More",-1)})),Mt={key:1,class:"card",style:{color:"red"}},Tt={class:"col-10"},Ct={class:"bg-grey"},Dt=ut((function(){return Object(n["h"])("h4",{class:"abc"},"Year",-1)})),$t={class:"rightright"},Ft=ut((function(){return Object(n["h"])("h4",{class:"def"},"More",-1)})),Nt={key:1,class:"card",style:{color:"red"}};function St(e,t,c,r,a,o){var i=Object(n["F"])("router-link"),s=Object(n["F"])("movie-card-container");return Object(n["y"])(),Object(n["g"])("div",ht,[Object(n["h"])("div",bt,[Object(n["h"])("div",jt,[dt,Object(n["h"])("div",Ot,[Object(n["j"])(i,{to:"/search?Title=".concat(e.search_params)},{default:Object(n["M"])((function(){return[vt]})),_:1},8,["to"])]),null!=this.title_movies?(Object(n["y"])(),Object(n["e"])(s,{key:0,movies:e.title_movies},null,8,["movies"])):Object(n["f"])("",!0),null==this.title_movies?(Object(n["y"])(),Object(n["g"])("div",pt," No result ")):Object(n["f"])("",!0)])]),Object(n["h"])("div",ft,[Object(n["h"])("div",mt,[gt,Object(n["h"])("div",yt,[Object(n["j"])(i,{to:"/search?Celebrity=".concat(e.search_params)},{default:Object(n["M"])((function(){return[_t]})),_:1},8,["to"])]),null!=this.celes_movies?(Object(n["y"])(),Object(n["e"])(s,{key:0,movies:e.celes_movies},null,8,["movies"])):Object(n["f"])("",!0),null==this.celes_movies?(Object(n["y"])(),Object(n["g"])("div",wt," No result ")):Object(n["f"])("",!0)])]),Object(n["h"])("div",kt,[Object(n["h"])("div",It,[xt,Object(n["h"])("div",Pt,[Object(n["j"])(i,{to:"/search?Genre=".concat(e.search_params)},{default:Object(n["M"])((function(){return[At]})),_:1},8,["to"])]),null!=this.genre_movies?(Object(n["y"])(),Object(n["e"])(s,{key:0,movies:e.genre_movies},null,8,["movies"])):Object(n["f"])("",!0),null==this.genre_movies?(Object(n["y"])(),Object(n["g"])("div",Mt," No result ")):Object(n["f"])("",!0)])]),Object(n["h"])("div",Tt,[Object(n["h"])("div",Ct,[Dt,Object(n["h"])("div",$t,[Object(n["j"])(i,{to:"/search?Year=".concat(e.search_params)},{default:Object(n["M"])((function(){return[Ft]})),_:1},8,["to"])]),null!=this.year_movies?(Object(n["y"])(),Object(n["e"])(s,{key:0,movies:e.year_movies},null,8,["movies"])):Object(n["f"])("",!0),null==this.year_movies?(Object(n["y"])(),Object(n["g"])("div",Nt," No result ")):Object(n["f"])("",!0)])])])}var qt={name:"MovieAllPage",components:{MovieCardContainer:Qe,MovieCard:He},created:function(){var e=this;console.log("MovieAllPage created"),this.$watch((function(){return e.$route.query.All}),(function(t,c){console.log("".concat(c,"->").concat(t)),void 0!=t&&(e.search_params=t,e.search())}),{immediate:!0})},data:function(){return{api:"api/movies/search",title_movies:null,celes_movies:null,genre_movies:null,year_movies:null,search_params:""}},methods:{search:function(){var e=this;console.log("Search"),window.scrollTo(0,0),fetch("".concat(this.api,"?All=").concat(this.search_params)).then((function(e){return e.json()})).then((function(t){"success"==t.response?(e.title_movies=t.movies.title,e.celes_movies=t.movies.celebrity,e.genre_movies=t.movies.genre,e.year_movies=t.movies.year):e.title_movies="fail"}))}}};c("153a");const Bt=i()(qt,[["render",St],["__scopeId","data-v-09c8d44e"]]);var Rt=Bt,Et=[{path:"/",name:"StartPage",component:me,meta:{keepAlive:!1}},{path:"/home",name:"Home",component:z,meta:{keepAlive:!0},children:[{path:"/search",name:"MovieListPage",component:lt,meta:{keepAlive:!1}},{path:"/notfound/:searchtxt",name:"NotFoundPage",component:Pe,props:!0,meta:{keepAlive:!1}},{path:"/movie/:id",name:"MovieInfoPage",component:se,props:!0,meta:{keepAlive:!1}},{path:"/searchAll",name:"MovieAllPage",component:Rt,meta:{keepAlive:!1}}]}],Gt=Object(u["a"])({history:Object(u["b"])("/"),routes:Et}),Kt=Gt,Ut=(c("f9e3"),c("4989"),c("f2e8"),Object(n["d"])(l));Ut.use(Kt),Ut.mount("#app")},6811:function(e,t,c){},6835:function(e,t,c){"use strict";c("e736")},6859:function(e,t,c){"use strict";c("86be")},8197:function(e,t,c){"use strict";c("ee68")},8491:function(e,t,c){e.exports=c.p+"static/img/logo.99d731b9.png"},"86be":function(e,t,c){},8820:function(e,t,c){"use strict";c("6811")},"9a14":function(e,t,c){"use strict";c("f444")},a1d9:function(e,t,c){"use strict";c("3856")},bf15:function(e,t,c){"use strict";c("313c")},cc76:function(e,t,c){"use strict";c("2e61")},e736:function(e,t,c){},ee68:function(e,t,c){},f444:function(e,t,c){}});
//# sourceMappingURL=app.42bd5e00.js.map