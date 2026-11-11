with operaciones_por_serie as(
	select 
		serie ,
		sum(case when Mes = '2024-12-01' then operaciones end) as operaciones_dic_2024,
		sum(case when Mes = '2025-12-01' then operaciones end) as operaciones_dic_2025
		from dbo.detalles_pagos2
		where serie in ('Niubiz QR','Izipay QR')
			AND MES IN ('2024-12-01','2025-12-01')
		GROUP BY Serie)

select serie , operaciones_dic_2024 , operaciones_dic_2025 , operaciones_dic_2025 - operaciones_dic_2024 AS aumento_millones ,
	100.0 * (operaciones_dic_2025 - operaciones_dic_2024) / 20 as porcentaje_de_aumento
from operaciones_por_serie
order by aumento_millones;
