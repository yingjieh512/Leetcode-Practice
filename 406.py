class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        copy_people = sorted(people, key=lambda x: (-x[0], x[1]))
        result = [copy_people[0]]

        for i in range(1, len(copy_people)):
            person = copy_people[i]

            if person[1] == 0:
                result.insert(0, person)
                continue

            infront = 0
            inserted = False

            for j in range(len(result)):
                if result[j][0] >= person[0]:
                    infront += 1

                if infront == person[1]:
                    result.insert(j + 1, person)
                    inserted = True
                    break
            if not inserted:
                result.append(person)

        return result