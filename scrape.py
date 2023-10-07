import requests
import json

def scrape():

    with open("82peaks.json") as peak_names_file:
        peak_names = json.load(peak_names_file)

    print("pulling peaks")
    for peak in peak_names:
        url = "https://www.mountain-forecast.com/peaks/" + peak + "/forecasts/data?elev=all&period_types=p,t,h"
        headers = {"accept": "application/json",
            "accept-language": "en-US,en;q=0.9,nl;q=0.8",
            "if-none-match": "W/\"d8c290306a60516c5853ef9ca31061b4\"",
            "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "cookie": "remember_token=; dnsDisplayed=undefined; ccpaApplies=false; signedLspa=undefined; euconsent-v2=CPnykoAPnykoAAGABCENC5CgAP_AAH_AABpYIJtf_X_fb3_j-_59__t0eY1f9_7_v-0zjhedk-8Nyd_X_L8X_2M7vB36pq4KuR4Eu3LBAQdlHOHcTUmw6IkVqTPsbk2Mr7NKJ7PEmnMbOydYGH9_n1XT_ZKY79____77_v-____37____-_f3_v5_1_--xAAAAAAAAAAAAAAAAAAAAAAggmAQYCAgAAAIIAAAQIAQgAAhBEgAAAACCAACgAQAJVAAErgIjAQAAEAgAhAABCCAhBgEAAAAASABACAFggEAAEAgABAAIAAAAIQAQEAFgIAAAIASEABEAEIEBBEAABSGBAQAEEAKAAAAAcSGAEAZZQAkCAAAAAAAAAAAAAAAAAAAAAACA2MgHABDACYAI4AZYBHACrgFbAWiAtgBcgDIwGcgM8AZ8NAAgLoGAAgE2ANqEQFwBDACXAGQAMsAbMA-wD8AIAARgAkwBTwCrgGsAOqAfIBDoCRAE7AKRAXIAyMBk4DOQGfCQAIC6BAAMAEgCbAG1BIJAACAAFwAUABUADIAHAAPAAgABgADKAGgAagA8gCGAIoATAAngBVADeAHMAPQAfgBDQCIAImASwBLgCaAFKALcAYYAyABlgDZAHeAPYAfEA-wD9gH-AgABFICLgIwARwAkwBKQCggFPAKuAXMAxQBrADaAG4AOIAegA-QCHQEiAJlATsAocBSICmgFigLQAWwAuQBd4DBgGGgMkAZOAy4BnIDPgGkQNYA1kBt4UACAIoIAKAA2ACQAH4BSwCzgGiATYApsBgQDag0BwALgAhgBLgDIAGWANmAfYB-AEAAIKARgAkwBTwCrwFoAWkA1gB1QD5AIdARMAioBIgCdgFIgLkAZOAzkBngDPg4AEBdAYAGAmwBTYDahUBAACgAQwAmABcAEcAMsAjgBV4C0ALSAtgBcgDIwGcgM8AZ8A3IWABAXQKABAJsAbUOgsgALgAoACoAGQAOAAgABdADAAMoAaABqADwAH0AQwBFACYAE8AKoAXAAxABmADeAHMAPQAfgBDQCIAImASwBLgCaAFGAKUAWIAt4BhAGGAMgAZQA0QBsgDvAHtAPsA_QB_gEUgIsAjEBHAEdAJMASkAoIBTwCrgFigLQAtIBcwC6gF5AMUAbQA3ABxADnAHUAPQAfYBDoCKgEXgJEASoAnYBQ4CmgFWALFAWwAuABcgC7QF3gMGAYaAx6BkYGSAMnAZUAywBlwDMwGcgM-AaIA0gBrADbx4AIARQBGRwAcAEgAUADMgJsAU2AtABtRCBqAAsACgAGQAXAAxABqAEMAJgAUwAqgBcADEAGYAN4AegBHAClAFiAMIAZQA7wB9gD_AIoARwAlIBQQCngFXgLQAtIBcwDFAG0AOcAdQA9ACRAEqAKaAVYAsUBaIC2AFwALkAXaAyMBk4DOQGeAM-AaIA4AiABAIyQACADNAMyAmwBtRKBoAAgABYAFAAMgAcAA_ADAAMQAeABEACYAFUALgAYgAzACGgEQARIAowBSgC3AGEAMoAbIA74B9gH4ARwAp4BV4C0ALSAXMAuoBigDcAHUAPkAh0BEwCKgEXgJEAWKAtgBdoDIwGTgMsAZyAzwBnwDSAGsANvAcATAAgEZJAAwBmgGZATYUghgALgAoACoAGQAOAAggBgAGUANAA1AB5AEMARQAmABPACkAFUAMQAZgA5gB-AENAIgAiQBRgClAFiALcAYQAyABlADRAGyAO-AfYB-gEWAIxARwBHQCUgFBAKuAVsAuYBeQDaAG4APQAfYBDoCJgEXgJEAScAnYBQ4CrAFigLYAXAAuQBdoDDYGRgZIAycBlgDLgGcgM8AZ8A0iBrAGsgNvKgAQA2lAAwAJAA_gEHAJOAmwBTY.YAAAAAAAAAAA; consentUUID=2944a46d-d29c-4a8d-b68e-5b8a237c07a3_17; ccpaUUID=16bf041c-7fde-416c-9dd2-f78ffa3d2e9f; _cc_id=ac0b9816a51e3303b34f349545f16f8c; euconsent-v2=CPy6fIAPy6fIAAKAwAENDZCsAP_AAH_AAAwIJrNV_H__bW9r8X7_aft0eY1P9_j77uQxBhfJE-4F3LvW_JwXx2E5NF36tqoKmRoEu3ZBIUNlHJHUTVmwaogVryHsak2cpTNKJ6BkkFMRM2dYCF5vm4tjeQKY5_p_d3fx2D-t_dv839z3z81Xn3d5f--0-PCdU5-9Dfn9fRfb-9IP9_78v8v8_l_rk2_eT13_pcvr_D--f_87_XW-8QUIKAACIAHAAeABcAD4AOAAugBoAD-AIQARwAywBmgDnAHcAQAAgcBBwEIAIiARoAn4BUACxAFnALqAXoAxQBnwDXgHHAOkAdQA7YB9gD_gIQgR4BHsCVQJWATFAmQCZQEzgJtAUgApMBVQCuwFhALKAWoAugBdsC8gLzAX0AwQBiADFgGQgMjAaIA0YBpoDUwGvANoAbZA24DbwG5AN0Ab4A4IB2wDuYIJggoBIgCSgEowJaATHAmSBNIIKAAA.YAAAAAAAAAAA; addtl_consent=1~43.3.9.6.9.13.6.4.15.9.5.2.11.1.7.1.3.2.10.33.4.6.9.17.2.9.20.7.20.5.20.6.3.2.1.4.11.29.4.14.9.3.10.6.2.9.6.6.9.8.29.4.5.3.1.27.1.17.10.9.1.8.6.2.8.3.4.146.65.1.17.1.18.25.35.5.18.9.7.41.2.4.18.24.4.9.6.5.2.14.18.7.3.2.2.8.28.8.6.3.10.4.20.2.13.4.10.11.1.3.22.16.2.6.8.6.11.6.5.33.11.8.1.10.28.12.1.5.19.9.6.40.17.4.9.15.8.7.3.12.7.2.4.1.7.12.13.22.13.2.14.10.1.4.15.2.4.9.4.5.4.7.13.5.15.4.13.4.14.10.15.2.5.6.2.2.1.2.14.7.4.8.2.9.10.18.12.13.2.18.1.1.3.1.1.9.25.4.1.19.8.4.8.5.4.8.4.4.2.14.2.13.4.2.6.9.6.3.2.2.3.5.2.3.6.10.11.6.3.19.11.3.1.2.3.9.19.26.3.10.7.6.4.3.4.6.3.3.3.3.1.1.1.6.11.3.1.1.11.6.1.10.5.8.3.2.2.4.3.2.2.7.15.7.14.1.3.3.4.5.4.3.2.2.5.5.1.2.9.7.9.1.5.3.7.10.11.1.3.1.1.2.1.3.2.6.1.12.8.1.3.1.1.2.2.7.7.1.4.3.6.1.2.1.4.1.1.4.1.1.2.1.8.1.7.4.3.3.3.5.3.15.1.15.10.28.1.2.2.12.3.4.1.6.3.4.7.1.3.1.4.1.5.3.1.3.4.1.5.2.3.1.2.2.6.2.1.2.2.2.4.1.1.1.2.2.1.1.1.1.2.1.1.1.2.2.1.1.2.1.2.1.7.1.4.1.2.1.1.1.1.2.1.4.2.1.1.9.1.6.2.1.6.2.3.2.1.1.1.2.5.2.4.1.1.2.2.1.1.7.1.2.2.1.2.1.2.3.1.1.2.4.1.1.1.5.1.3.6.3.1.5.5.4.1.2.3.1.4.3.2.2.3.1.1.1.1.1.11.1.3.1.1.2.2.5.2.3.3.5.2.7.1.1.2.5.1.9.5.1.3.1.8.4.5.1.9.1.1.1.2.1.1.1.4.2.13.1.1.3.1.2.2.3.1.2.1.1.1.2.1.3.1.1.1.1.2.4.1.5.1.2.4.3.8.2.2.9.7.2.2.1.2.1.3.1.6.1.7.1.1.2.6.3.1.2.1.200.200.100.100.200.400.100.100.100.200.200.1700.100.204.596.100.1000.800.500.400.200.200.500.1300.801.99; panoramaId_expiry=1696670717162; panoramaId=3cda3fa44ff0c5f98d200869b2674945a7029b2d9f10b661a6b74c4aa31e3243; panoramaIdType=panoIndiv; _gid=GA1.2.404596600.1696276074; last_loc=1338; _gat_UA-226744-23=1; cto_bundle=j0fjTV90a3AxMDJweVVodU81TFdPb1RmN0w0cmo2UjU5SGZ0OTlGbGxWJTJCbWczJTJCYmolMkJaUyUyQnNrUU9wOFJVcTMwSEJybHRmZjkxcjI4QUtVbzc5SExwbFJydXpxYUN3cmglMkZEd24zY1FVVmklMkZxY1FFRXlmbGhrUTRrbyUyRll2dFBjNDVReTU3VVA4eiUyQnNhTTJRU21NRlR0JTJGQyUyRllrcnhTbjN3TkV2MllBRTUlMkZaRW5tTU93JTNE; _mtn_session=eTFyMnNVQ2dSNzBRYTJGUW5sUjl1MEtGbm5hWlhlVmlXbFFTcFhTclBQenFtMXBMWDdZMU9vaXZyOHdwUnRNTW1QME8yYWs3bnBFUDZDWDFkZlVGVjRmV21WRkRDTGI4MXUzdFpiQkE4WXFxTkV3T3kvelJSQmxML3h1Ymg1MXp4NFIyNEZiTjVXNWNqM1JIcmxySzE2UWZWVDRlSExvUjJHL2g3MkN6RTNDeWIvcDE1SmM3STF5dnIvL3FIZ2JqZFVYaHE1NUNRSEV5cmNZdFhtN20zVkdVMzBtNlR2dFFudmpZZ1prQWxCQT0tLTBJZjdlWjFhOWpLcGZITzF1RUNwOGc9PQ%3D%3D--21a720bd1d91f624a4c0e1d23193f4f6a7c6322f; _ga_Z14L0E9BG8=GS1.1.1696445800.19.1.1696445813.47.0.0; _ga=GA1.2.853306046.1689190132",
            "Referer": "https://www.mountain-forecast.com/peaks/Matterhorn/forecasts/4478",
            "Referrer-Policy": "strict-origin-when-cross-origin"}

        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print("There has been a problem")
            print(peak)
            print(res.status_code)
        json_object = json.dumps(res.json())

        with open("scrape_responses/" + peak + ".json", "w") as outfile:
            outfile.write(json_object)

    print("scraping complete")