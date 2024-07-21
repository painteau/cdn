const start_html = '<table class="table"><tbody><tr class="tr-header"><td class="td0"><img src="https://cdn.painteau.com/img/ratp/logo-bus.png" alt="" class="rer-logo" /></td><td class="td1"><p>Station: Parc du Tremblay</p></td><td colspan="3" class="td2-header"><p>23:03</p></td></tr>';
let main_html = '';

const end_html = '<tr class="tr-trafic"><td class="tdfull" colspan="4"><p><i>Attention traffic</i></p></td></tr></tbody></table>';

for (const item of $input.all()) {
    main_html += `<tr class="tr-normal"><td class="td0"><img src="https://cdn.painteau.com/img/ratp/${item.json['ligne']}.png" alt="" class="rer-ligne" /></td><td class="td1"><p>${item.json['Direction']}</p></td><td class="td2"><p>${item.json['minutes']}</p></td><td class="td3 "></td></tr>`;
}

return [{
    json: {
        table_html: start_html + main_html + end_html
    }
}]