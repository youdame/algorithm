

SELECT CONCAT('/home/grep/src/', F.BOARD_ID,'/', FILE_ID,  FILE_NAME , FILE_EXT) as FILE_PATH
from USED_GOODS_FILE F
join USED_GOODS_BOARD  B 
ON B.board_id= f.board_id
where (views) = (select max(views)
from USED_GOODS_BOARD)
order by file_id desc