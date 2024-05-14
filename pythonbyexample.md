<h3 id="program-1">Program 1</h3>
<p>This program asks the user for a distance in miles and converts it to kilometres.</p>
<pre class=" language-python"><code class="prism  language-python">miles <span class="token operator">=</span> <span class="token builtin">float</span><span class="token punctuation">(</span><span class="token builtin">input</span><span class="token punctuation">(</span><span class="token string">"Enter distance in miles: "</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"That's "</span> <span class="token operator">+</span> <span class="token builtin">str</span><span class="token punctuation">(</span>miles <span class="token operator">*</span> <span class="token number">1.60934</span><span class="token punctuation">)</span> <span class="token operator">+</span> <span class="token string">" kilometres."</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="program-2">Program 2</h3>
<p>This program does the same as Program 1.</p>
<pre class=" language-python"><code class="prism  language-python">miles <span class="token operator">=</span> <span class="token builtin">float</span><span class="token punctuation">(</span><span class="token builtin">input</span><span class="token punctuation">(</span><span class="token string">"Enter distance in miles: "</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"That's {} kilometres."</span><span class="token punctuation">.</span><span class="token builtin">format</span><span class="token punctuation">(</span>miles <span class="token operator">*</span> <span class="token number">1.60934</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="program-3">Program 3</h3>
<p>


```Python
miles = float(input("Enter distance in miles: "))
print("That's " + str(miles * 1.60934) + " kilometres."This program does the same as Program 1.


```Python
miles = float(input("Enter distance in miles: "))
print("That's {} kilometres.".format(miles * 1.60934))
```


### Program 3


This program asks the user to enter a character and tells them if it was a vowel or not. Note that it is case insensitive and it prints an appropriate message if the user didn’t enter a letter or entered more than a single character.</p>
<pre class=" language-python"><code class="prism  language-python">letter <span class="token operator">=</span> <span class="token builtin">input</span><span class="token punctuation">(</span><span class="token string">"Enter a letter: "</span><span class="token punctuation">)</span>


<span class="token keyword">if</span> letter<span class="token punctuation">.</span>isalpha<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">and</span> <span class="token builtin">len</span><span class="token punctuation">(</span>letter<span class="token punctuation">)</span> <span class="token operator">==</span> <span class="token number">1</span><span class="token punctuation">:</span>
    <span class="token keyword">if</span> letter<span class="token punctuation">.</span>lower<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">in</span> <span class="token string">"aeiou"</span><span class="token punctuation">:</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"You entered a vowel."</span><span class="token punctuation">)</span>
    <span class="token keyword">else</span><span class="token punctuation">:</span>
        <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"You didn't enter a vowel."</span><span class="token punctuation">)</span>
<span class="token keyword">else</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"You didn't enter a letter."</span><span class="token punctuation">)</span>
</code></pre>
<p><strong>Task:</strong></p>
<ol>
<li>


```Python
letter = input("Enter a letter: ")


if letter.isalpha() and len(letter) == 1:
    if letter.lower() in "aeiou":
        print("You entered a vowel.")
    else:
        print("You didn't enter a vowel.")
else:
    print("You didn't enter a letter.")
```


**Task:**


1. Write a program that asks the user to enter a number and then asks them to enter C or F. If they enter C it should convert the number from Fahrenheit to Celsius and print the result. If they enter an F it should convert the number from Celsius to Fahrenheit and print the result. It should be case insensitive and if they enter neither C nor F it should print an appropriate message.</li>
</ol>
<h3 id="program-1-1">Program 1</h3>
<p>


### Program 1


This program asks the user for their name and then says hello to them and tells them how many letters are in their name.</p>
<pre class=" language-python"><code class="prism  language-python">name <span class="token operator">=</span> <span class="token builtin">input</span><span class="token punctuation">(</span><span class="token string">"Enter your name: "</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"Hello "</span> <span class="token operator">+</span> name <span class="token operator">+</span> <span class="token string">". Your name has "</span> <span class="token operator">+</span> <span class="token builtin">str</span><span class="token punctuation">(</span><span class="token builtin">len</span><span class="token punctuation">(</span>name<span class="token punctuation">)</span><span class="token punctuation">)</span> <span class="token operator">+</span> <span class="token string">" letters in it."</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="program-2-1">Program 2</h3>
<p>This program does the same as Program 1.</p>
<pre class=" language-python"><code class="prism  language-python">name <span class="token operator">=</span> <span class="token builtin">input</span><span class="token punctuation">(</span><span class="token string">"Enter your name: "</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"Hello {}. Your name has {} letters in it."</span><span class="token punctuation">.</span><span class="token builtin">format</span><span class="token punctuation">(</span>name<span class="token punctuation">,</span> <span class="token builtin">len</span><span class="token punctuation">(</span>name<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="program-3-1">Program 3</h3>
<p>


```Python
name = input("Enter your name: ")
print("Hello " + name + ". Your name has " + str(len(name)) + " letters in it.")
```


### Program 2


This program does the same as Program 1.


```Python
name = input("Enter your name: ")
print("Hello {}. Your name has {} letters in it.".format(name, len(name)))
```


### Program 3


This program asks the user for two numbers and then tells the user which of the numbers was the larger.</p>
<pre class=" language-python"><code class="prism  language-p


```Python">
n1 <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span><span class="token builtin">input</span><span class="token punctuation">(</span><span class="token string">"Enter first number: "</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
n2 <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span><span class="token builtin">input</span><span class="token punctuation">(</span><span class="token string">"Enter second number: "</span><span class="token punctuation">)</span><span class="token punctuation">)</span>


<span class="token keyword">if</span> n1 <span class="token operator">&gt;</span> n2<span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"The first number is greater than the second."</span><span class="token punctuation">)</span>
<span class="token keyword">elif</span> n2 <span class="token operator">&gt;</span> n1<span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"The second number is greater than the first."</span><span class="token punctuation">)</span>
<span class="token keyword">else</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"The numbers are the same."</span><span class="token punctuation">)</span>
</code></pre>
<p><strong>Task:</strong></p>
<ol>
<li>= int(input("Enter first number: "))
n2 = int(input("Enter second number: "))


if n1 > n2:
    print("The first number is greater than the second.")
elif n2 > n1:
    print("The second number is greater than the first.")
else:
    print("The numbers are the same.")
```


**Task:**


1. Write a program that asks the user to enter two words and then prints the longer of the two words. If the words are of the same length it should display an appropriate message along with both words.</li>
</ol>

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY5MzkzMjk0OV19
-->