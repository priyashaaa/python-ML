def starts_with_prefix(string, prefix):
    return string.startswith(prefix)

def ends_with_suffix(string, suffix):
    return string.endswith(suffix)

string = "hello world"
prefix = "hello"
suffix = "world"

print(f"Does '{string}' start with '{prefix}'? {starts_with_prefix(string, prefix)}")
print(f"Does '{string}' end with '{suffix}'? {ends_with_suffix(string, suffix)}")