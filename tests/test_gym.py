from storage import save_members, load_members

test_members = [{
    "id": "TEST001",
    "name": "Test User",
    "age": "20",
    "phone": "9876543210"
}]

save_members(test_members)
assert load_members() == test_members
print("Storage test passed.")

# Reset test data so the real project starts empty.
save_members([])
