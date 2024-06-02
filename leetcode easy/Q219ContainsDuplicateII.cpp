class Solution1 {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int n=nums.size();
        pair<int,int> p[n];
        for(int i=0;i<n;i++) {
            p[i] = {nums[i],i};
        }
        sort(p,p+n);
        for(int i=1;i<n;i++) {
            if(p[i].first == p[i-1].first) {
                if(p[i].second - p[i-1].second <= k) return true;
                else continue;
            }
        }
        return false;
    }
};
class Solution2 {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> found;
        for (int i = 0; i < nums.size(); i++) {
            if (found.count(nums[i])) {
                if (abs(i - found[nums[i]]) <= k) {
                    return true;
                }
            }
            found[nums[i]] = i;
        }
        return false;
    }
};

static const int _ = []() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 0;
}();
#define SHIFT_FACTOR 2

unsigned long long FIXED_RANDOM;

struct HashSet {
    int* values;
    int capacity;
    int size;
};

int resize_counter = 0;

unsigned _hash(int x) {
    return x + FIXED_RANDOM;
}

void allocate(struct HashSet* set, int num_itens) {
    set->capacity = 1 << (32 - __builtin_clz(num_itens) + SHIFT_FACTOR);
    set->values = (int*)malloc(set->capacity * sizeof(int));
    set->size = 0;
    for (int i = 0; i < set->capacity; i++) {
        set->values[i] = INT_MIN;
    }
}

void init(struct HashSet* set) {
    srand(time(NULL));
    FIXED_RANDOM = ((unsigned long long)rand() << 32) | rand();
    allocate(set, 1);
}

int get_index(struct HashSet* set, int val) {
    int mask = set->capacity - 1;
    int idx = _hash(val) & mask;
    while (set->values[idx] != val && set->values[idx] != INT_MIN) {
        idx = (idx + 1) & mask;
    }
    return idx;
}

bool find(struct HashSet* set, int val) {
    int idx = get_index(set, val);
    return set->values[idx] == val;
}

void _insert(struct HashSet* set, int val) {
    int idx = get_index(set, val);
    if (set->values[idx] == INT_MIN) {
        set->values[idx] = val;
        set->size++;
    }
}

void resize(struct HashSet* set, int new_size) {
    int* old_values = set->values;
    int old_capacity = set->capacity;
    allocate(set, new_size);
    for (int i = 0; i < old_capacity; i++) {
        if (old_values[i] != INT_MIN) {
            _insert(set, old_values[i]);
        }
    }
    free(old_values);
    resize_counter++;
}

void insert(struct HashSet* set, int val) {
    if ((set->capacity >> SHIFT_FACTOR) < set->size + 1) {
        resize(set, set->size + 1);
    }
    _insert(set, val);
}

void erase(struct HashSet* set, int val) {
    int idx = get_index(set, val);
    if (set->values[idx] == val) {
        set->values[idx] = INT_MIN;
        set->size--;
    }
}

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        struct HashSet* set = (struct HashSet*)malloc(sizeof(struct HashSet));
        init(set);
        for (int i = 0; i < nums.size(); i++) {
            if (find(set, nums[i])) {
                return true;
            }
            insert(set, nums[i]);
            if (i >= k) {
                erase(set, nums[i - k]);
            }
        }
        return false;
    }
};