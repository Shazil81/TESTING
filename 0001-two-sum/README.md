<h2><a href="https://leetcode.com/problems/two-sum/submissions/2139470489/">1. Two Sum</a></h2><h3>Difficulty: Easy</h3><hr>p<b>Runtime:</b> N/A | <b>Memory:</b> N/A</p><hr><p>You are given an array of integers <code style="background-color: #f7f7f9; color: #262626; padding: 2px 6px; border-radius: 4px; font-family: monospace;">nums</code>&nbsp;and an integer <code style="background-color: #f7f7f9; color: #262626; padding: 2px 6px; border-radius: 4px; font-family: monospace;">target</code>, return <em>indices of the two numbers such that they add up to <code style="background-color: #f7f7f9; color: #262626; padding: 2px 6px; border-radius: 4px; font-family: monospace;">target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="background-color: #f7f8fa; padding: 12px; border-radius: 8px; font-family: monospace; border: 1px solid #e5e7eb;"><strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="background-color: #f7f8fa; padding: 12px; border-radius: 8px; font-family: monospace; border: 1px solid #e5e7eb;"><strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre style="background-color: #f7f8fa; padding: 12px; border-radius: 8px; font-family: monospace; border: 1px solid #e5e7eb;"><strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code style="background-color: #f7f7f9; color: #262626; padding: 2px 6px; border-radius: 4px; font-family: monospace;">2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code style="background-color: #f7f7f9; color: #262626; padding: 2px 6px; border-radius: 4px; font-family: monospace;">-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code style="background-color: #f7f7f9; color: #262626; padding: 2px 6px; border-radius: 4px; font-family: monospace;">-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code style="background-color: #f7f7f9; color: #262626; padding: 2px 6px; border-radius: 4px; font-family: monospace;">O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?