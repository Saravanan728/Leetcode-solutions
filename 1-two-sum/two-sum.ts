function twoSum(nums: number[], target: number): number[] {
    // const map=new Map<number,number>();
    // for (let i=0;i<nums.length;i++){
    //     const comp=target-nums[i];
    //     if(map.has(comp)){
    //         return[map.get(comp)!,i];
    //     }
    //     map.set(nums[i],i);
    // }
    // return[];

    const arr=nums.map((value,index)=>({value,index}));
    arr.sort((a,b)=>a.value-b.value);

    let left:number =0;
    let right:number=nums.length-1;

    while (left<right){
        const sum=arr[left].value+arr[right].value;
        if(sum===target){
            return[arr[left].index,arr[right].index];

        }

        if(sum<target){
            left++;

        }else{
            right--;
        }

    }
    return[];
    
};