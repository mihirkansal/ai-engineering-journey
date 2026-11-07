def in_flight(qps, latency_ms):
    return (qps * latency_ms) / 1000

if __name__ == "__main__":
    print(in_flight(400, 50))
    print(in_flight(120, 35))
    print(in_flight(40, 35))
