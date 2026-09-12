<h2><a href="https://leetcode.com/problems/two-sum/submissions/2139356627/">0001 TWO SUM</a></h2><h3>Difficulty: Easy</h3><hr><p>You are given an array of integers `nums`&nbsp;and an integer `target`, return <em>indices of the two numbers such that they add up to `target`</em>.</p>

<p>You may assume that each input would have <b><em>exactly</em> one solution</b>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</b></p>

<pre><b>Input:</b> nums = [2,7,11,15], target = 9
<b>Output:</b> [0,1]
<b>Explanation:</b> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</b></p>

<pre><b>Input:</b> nums = [3,2,4], target = 6
<b>Output:</b> [1,2]
</pre>

<p><strong class="example">Example 3:</b></p>

<pre><b>Input:</b> nums = [3,3], target = 6
<b>Output:</b> [0,1]
</pre>

<p>&nbsp;</p>
<p><b>Constraints:</b></p>

<ul>
	<li>`2 &lt;= nums.length &lt;= 10<sup>4</sup>`</li>
	<li>`-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup>`</li>
	<li>`-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup>`</li>
	<li><b>Only one valid answer exists.</b></li>
</ul>

<p>&nbsp;</p>
<b>Follow-up:&nbsp;</b>Can you come up with an algorithm that is less than `O(n<sup>2</sup>)`<font face="monospace">&nbsp;</font>time complexity?