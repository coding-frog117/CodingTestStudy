function solution(user_id, banned_id) {
  let answer = 0;
  let set = new Set();

  function DFS(bannedIndex, selectedUsers, selectedUserIds) {
    if (bannedIndex === banned_id.length) {
      let sortedUserIds = selectedUserIds.split(" ").slice(1).sort().join("");
      set.add(sortedUserIds);
      return;
    }

    for (let i = 0; i < user_id.length; i++) {
      if (selectedUsers[i] || banned_id[bannedIndex].length !== user_id[i].length) continue;
      if (!compareString(banned_id[bannedIndex], user_id[i])) continue;

      selectedUsers[i] = true;
      DFS(bannedIndex + 1, selectedUsers, selectedUserIds + " " + user_id[i]);
      selectedUsers[i] = false;
    }
  }

  DFS(0, Array(user_id.length).fill(false), "");
  console.log(set);

  return set.size;
}

function compareString(string1, string2) {
  for (let i = 0; i < string1.length; i++) {
    if (string1[i] !== "*" && string1[i] !== string2[i]) {
      return false;
    }
  }
  return true;
}

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]);
