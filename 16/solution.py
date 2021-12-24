from typing import Tuple, List


def parse_literal(binary_data: str) -> Tuple[int, str]:
    start_i = 0
    end_i = 5
    final_blob = ""
    parsed_len = 0

    while True:
        chunk = binary_data[start_i:end_i]
        final_blob += chunk[1:]
        parsed_len += 5
        if chunk[0] == "0":
            break
        start_i += 5
        end_i += 5

    return int(final_blob, 2), binary_data[parsed_len:]


def parse_operator(binary_data: str) -> Tuple[int, str]:
    length_type_id = int(binary_data[:1], 2)
    remaining = binary_data[1:]
    return length_type_id, remaining


def parse_num_subpackets(binary_data: str) -> Tuple[int, str]:
    num_data = binary_data[:11]
    remaining = binary_data[11:]
    return int(num_data, 2), remaining


def parse_len_subpackets(binary_data: str) -> Tuple[int, str]:
    len_data = binary_data[:15]
    remaining = binary_data[15:]
    return int(len_data, 2), remaining


def parse_packet(binary_data: str) -> Tuple[int, int, str]:
    version = int(binary_data[:3], 2)
    type_id = int(binary_data[3:6], 2)
    remaining = binary_data[6:]

    if type_id == 4:
        final_value, remaining = parse_literal(remaining)
    else:
        lti, remaining = parse_operator(remaining)

        values: List[int] = []

        if lti == 0:
            length, remaining = parse_len_subpackets(remaining)
            split = remaining[:length]
            remaining = remaining[length:]

            while split:
                v, val, split = parse_packet(split)
                values.append(val)
                version += v
        elif lti == 1:
            num_subpackets, remaining = parse_num_subpackets(remaining)

            for i in range(num_subpackets):
                v, val, remaining = parse_packet(remaining)
                values.append(val)
                version += v
        else:
            raise ValueError("unuspported length type ID")

        final_value = 0

        if type_id == 0:  # sum
            for v in values:
                final_value += v
        elif type_id == 1:  # product
            final_value = 1
            for v in values:
                final_value *= v
        elif type_id == 2:  # min
            final_value = min(values)
        elif type_id == 3:  # max
            final_value = max(values)
        elif type_id == 5:  # gt
            assert len(values) == 2
            final_value = 1 if values[0] > values[1] else 0
        elif type_id == 6:  # lt
            assert len(values) == 2
            final_value = 1 if values[0] < values[1] else 0
        elif type_id == 7:  # eq
            assert len(values) == 2
            final_value = 1 if values[0] == values[1] else 0
        else:
            raise ValueError(f"Invalid type ID: {type_id}")

    return version, final_value, remaining


def main():
    bin_string = ""
    def hex_to_bin(hex_d): return bin(int(hex_d, 16))[2:].zfill(len(hex_d) * 4)

    with open("input16") as f:
        lines = f.readlines()
        stream = lines[0].rstrip("\n")

        for d in stream:
            bin_string += hex_to_bin(d)

    version, val, payload = parse_packet(bin_string)

    print(f"P1: {version}")
    print(f"P2: {val}")


if __name__ == "__main__":
    main()
