class logger:
    def info(msg:str):
        print(msg)






helmet_veloc = int(input("투구 속도 입력(마일):"))

helmet_km = round(1.069 * helmet_veloc,1)

logger.info("투구 속도는" + str(helmet_km) + "입니다.")






