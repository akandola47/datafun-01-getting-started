"""Arshpreet Kandola
September 3 2023"""

import math


from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def get_area_of_house_lot(length,width):
     logger.info(f"CALLING get_area_of_house_lot({length,width})")

    try: 
        area = length * width
        logger.info(f"The area of house lot is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
 
country_lot = get_area_of_house_lot(2000,5000)
downtown_lot = get_area_of_house_lot(1000,2000)
suburb_lot = get_area_of_house_lot(3000,3000)
farm_lot = get_area_of_house_lot(6000,7000)

logger.info(f"sum of all lots combined = {math.fsum(all_areas)}")
logger.info(f"abs differnce of country and farm lots = {math.fabs(country_lot - farm_lot)}")
logger.info(f"smallest lot = {min{all_lots}}")


logger.info("Explore some functions in the math module")
logger.info(f"math.comb(2000,5000) = {math.comb(2000,5000)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

