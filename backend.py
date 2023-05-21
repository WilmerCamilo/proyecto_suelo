def calcular_resultados(peso_total, peso_solidos, gravedad_especifica, volumen_total):
    if peso_solidos != 0:
        peso_unitario_agua = 1000  # kg/m^3

        peso_agua = peso_total - peso_solidos
        volumen_agua = peso_agua / peso_unitario_agua

        if peso_unitario_agua != 0:
            volumen_particulas_solidas = peso_solidos / (gravedad_especifica * peso_unitario_agua)

            volumen_vacios = volumen_total - volumen_particulas_solidas
            volumen_aire = volumen_vacios - volumen_agua
            humedad = peso_agua / peso_solidos * 100

            if volumen_particulas_solidas != 0:
                relacion_vacios = volumen_vacios / volumen_particulas_solidas
                porosidad = volumen_vacios / volumen_total

                peso_unitario_humedo = peso_total / volumen_total
                peso_unitario_seco = peso_solidos / volumen_total

                if volumen_vacios != 0:
                    saturacion_relativa = volumen_agua / volumen_vacios * 100

                    # Crear un diccionario con los resultados
                    resultados = {
                        'volumen_total': volumen_total,
                        'volumen_vacios': volumen_vacios,
                        'volumen_aire': volumen_aire,
                        'volumen_agua': volumen_agua,
                        'volumen_particulas_solidas': volumen_particulas_solidas,
                        'peso_humedo': peso_total,
                        'peso_agua': peso_agua,
                        'peso_seco': peso_solidos,
                        'humedad': humedad,
                        'relacion_vacios': relacion_vacios,
                        'porosidad': porosidad,
                        'peso_unitario_humedo': peso_unitario_humedo,
                        'peso_unitario_particulas_solidas': gravedad_especifica * peso_unitario_agua,
                        'peso_unitario_seco': peso_unitario_seco,
                        'gravedad_especifica': gravedad_especifica,
                        'saturacion_relativa': saturacion_relativa
                    }
                    

                    return resultados

    # Si hay algún valor cero, se devuelve None
    return None
