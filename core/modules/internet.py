import speedtest

def internet(query):
    import speedtest
    st = speedtest.Speedtest()
    down = st.download()
    up = st.upload()
    down = down / 1000000
    up = up / 1000000
    result = f"Download speed is {down} Mbps and Upload speed is {up} Mbps"
    return result