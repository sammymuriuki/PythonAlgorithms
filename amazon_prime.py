'''
Amazon Prime Video is a subscription video-on-demand over-the-top streaming 
and rental service. At Prime Video, the product team is creating a family plan 
for shared use. An Amazon business analyst needs to compute the pairs of family 
login strings as part of an analysis of the family plan adoption. The analyst 
has an array of strings, logins, where the lengths of all strings are equal. 
A string can be transformed one time by rotating its characters right by one step.
 In other words, change character 'a' to 'b', 'b' to 'c' and so on through changing 
 character 'z' to 'a'. Two strings logins[i] and logins[j] are called family logins 
 if one of them can be transformed into another. As an example, strings ("bcd","abc")
  are family logins because each character in "bcd" is one above the characters in "abc".
   The pairs ("abc","abc"), ("abc","acd") are not family logins. Find the number of pairs 
   of strings (i, j) which are family logins. Note that any pair of strings can be for a 
   login pair if the above condition is met. ExampleLet the array of strings 
   logins = ["bag", "sfe", "cbh", "cbh", "red"]. The following are the pairs of family
    login strings:indices (1, 3) that is "bag" and "cbh", after applying the above operation 
    to "bag" we obtain the string "cbh"indices (1, 4) that is "bag" and "cbh"indices (2, 5) 
    that is "sfe" and "red" Return 3, the number of pairs. Function DescriptionComplete the
     function countFamilyLogins in the editor below. countFamilyLogins has the following parameter: 
     string logins[n]: the password strings Returns int: the number of pairs of strings (i, j) 
     which are family logins. Constraints1 ≤ n ≤ 105The sum of lengths of all strings does not 
     exceed 2 · 105.The lengths of all n strings are equal.The strings contain lowercase letters only. 
     Input Format For Custom TestingSample Case 0
     Sample Input For Custom TestingSTDIN FUNCTION ----- -------5 → 
     logins[] size n = 5 corn → logins = ["corn", "horn", "dpso", "eqtp", "corn"] horndpsoeqtpcorn
     Sample Output3ExplanationThe pairs of sibling strings are:indices (1, 3) that is "corn" and "dpso".indices (3, 4) 
     that is "dpso" and "eqtp".indices (3, 5) that is "dpso" and "corn".
     '''
