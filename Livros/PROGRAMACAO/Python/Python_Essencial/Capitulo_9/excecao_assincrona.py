async def exemplo_assincrono():
    try:
        await alguma_funcao()
        
    except Exception as erro:
        raise MinhaExcecao("Erro assíncrono") from erro