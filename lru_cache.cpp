// https://leetcode.com/problems/lru-cache/
#include <unordered_map>
#include <list>
#include <utility>

class LRUCache {
private:
    typedef std::pair<int,int> cachePairType;
    typedef std::unordered_map <int, std::list<cachePairType>::iterator> cacheMapType;
    
    std::list <cachePairType> cacheList;
    cacheMapType cacheMap;
    int cacheSize;
    
public:
    
    LRUCache(int capacity) {
        cacheSize = capacity;
    }
    
    int get(int key) {
        cacheMapType::iterator cacheIt = cacheMap.find(key);
        
        if (cacheIt != cacheMap.end())
        {
            cachePairType item = *cacheIt->second;
            
            // Update the list
            cacheList.erase(cacheIt->second);
            cacheList.push_front(item);
            
            // Update the map with the new iterator
            cacheIt->second = cacheList.begin();
            
            return item.second;
        }
        else
        {
            return -1;
        }
        
    }
    
    void put(int key, int value) {
        std::pair item(key,value);
        cacheMapType::iterator cacheIt = cacheMap.find(key);
        
        if (cacheIt != cacheMap.end())
        {
            // Update the list
            cacheList.erase(cacheIt->second);
            cacheList.push_front(item);
            
            // Update the map with the new iterator
            cacheIt->second = cacheList.begin();
        }
        else
        {
            if(cacheList.size() >= cacheSize)
            {
                // Remove the item from both the map and list
                cachePairType evictedItem = cacheList.back();
                cacheMap.erase(cacheMap.find(evictedItem.first));
                cacheList.pop_back();
                
            }
            
            // Insert item in list and update map
            cacheList.push_front(item);
            cacheMap[key] = cacheList.begin();
        }
        
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
